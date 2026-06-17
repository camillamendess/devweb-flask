from database import get_connection
from models.minicurso import Minicurso

# DAO de minicursos - responsável por realizar as operações de acesso ao banco de dados relacionadas aos minicursos
class MinicursoDAO:

    # Método que lista todos os minicursos cadastrados no banco, ordenados alfabeticamente pelo nome
    def listar_todos(self):
        conn = get_connection()
        cursor = conn.execute("SELECT id, nome FROM minicursos ORDER BY nome")
        rows = cursor.fetchall()
        conn.close()
        return [Minicurso(row['id'], row['nome']) for row in rows]

    # Método que busca um minicurso específico pelo seu ID, retornando None caso não seja encontrado
    def buscar_por_id(self, id):
        conn = get_connection()
        cursor = conn.execute("SELECT id, nome FROM minicursos WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        return Minicurso(row['id'], row['nome']) if row else None

    # Método que salva um novo minicurso no banco com seu nome
    def salvar(self, minicurso):
        conn = get_connection()
        conn.execute("INSERT INTO minicursos (nome) VALUES (?)", (minicurso.nome,))
        conn.commit()
        conn.close()

    # Método que atualiza o nome de um minicurso existente no banco identificado pelo seu ID
    def atualizar(self, minicurso):
        conn = get_connection()
        conn.execute("UPDATE minicursos SET nome = ? WHERE id = ?", (minicurso.nome, minicurso.id))
        conn.commit()
        conn.close()

    # Método que remove um minicurso do banco pelo seu ID
    def deletar(self, id):
        conn = get_connection()
        conn.execute("DELETE FROM minicursos WHERE id = ?", (id,))
        conn.commit()
        conn.close()