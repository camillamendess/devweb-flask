# database.py
import sqlite3

DATABASE_NAME = "inscritos.db"

def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.execute("PRAGMA foreign_keys = ON;") # Força o SQLite a respeitar as regras de integridade e cascata
    conn.row_factory = sqlite3.Row  # Permite acessar colunas pelo nome!
    return conn

def init_db():
    conn = get_connection()
    # Criando tabela de minicursos primeiro
    conn.execute("""
        CREATE TABLE IF NOT EXISTS minicursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE
        )
    """)
    # Criando tabela de inscritos
    conn.execute("""
        CREATE TABLE IF NOT EXISTS inscritos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            minicurso_id INTEGER,
            FOREIGN KEY(minicurso_id) REFERENCES minicursos(id) ON DELETE CASCADE
        )
    """)
    
    # Inserindo dados iniciais padrão se a tabela de cursos estiver vazia
    cursor = conn.execute("SELECT COUNT(*) FROM minicursos")
    if cursor.fetchone()[0] == 0:
        cursos_iniciais = [("Java",), ("Python",), ("Javascript",), ("Typescript",)]
        conn.executemany("INSERT INTO minicursos (nome) VALUES (?)", cursos_iniciais)
        
    conn.commit()
    conn.close()