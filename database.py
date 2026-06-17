import sqlite3

# Nome do arquivo do banco de dados SQLite utilizado pela aplicação
DATABASE_NAME = "inscritos.db"

# Função que abre e retorna uma conexão com o banco de dados, com suporte a chaves estrangeiras e acesso às colunas pelo nome
def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    # Força o SQLite a respeitar as regras de integridade referencial e cascata entre tabelas
    conn.execute("PRAGMA foreign_keys = ON;")
    # Permite acessar os resultados das queries pelo nome da coluna em vez do índice
    conn.row_factory = sqlite3.Row
    return conn

# Função que inicializa o banco de dados, criando as tabelas e inserindo dados iniciais caso ainda não existam
def init_db():
    conn = get_connection()
    # Cria a tabela de minicursos primeiro, pois é referenciada pela tabela de inscritos via chave estrangeira
    conn.execute("""
        CREATE TABLE IF NOT EXISTS minicursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE
        )
    """)
    # Cria a tabela de inscritos com chave estrangeira para minicursos, aplicando exclusão em cascata
    conn.execute("""
        CREATE TABLE IF NOT EXISTS inscritos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            minicurso_id INTEGER,
            FOREIGN KEY(minicurso_id) REFERENCES minicursos(id) ON DELETE CASCADE
        )
    """)

    # Insere os minicursos iniciais padrão apenas se a tabela estiver vazia, evitando duplicatas
    cursor = conn.execute("SELECT COUNT(*) FROM minicursos")
    if cursor.fetchone()[0] == 0:
        cursos_iniciais = [("Java",), ("Python",), ("Javascript",), ("Typescript",)]
        conn.executemany("INSERT INTO minicursos (nome) VALUES (?)", cursos_iniciais)
        
    conn.commit()
    conn.close()