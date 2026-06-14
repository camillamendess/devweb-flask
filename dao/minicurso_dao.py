from database import get_connection
from models.minicurso import Minicurso

class MinicursoDAO:
    def listar_todos(self):
        conn = get_connection()
        cursor = conn.execute("SELECT id, nome FROM minicursos ORDER BY nome")
        rows = cursor.fetchall()
        conn.close()
        return [Minicurso(row['id'], row['nome']) for row in rows]

    def buscar_por_id(self, id):
        conn = get_connection()
        cursor = conn.execute("SELECT id, nome FROM minicursos WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        return Minicurso(row['id'], row['nome']) if row else None

    def salvar(self, minicurso):
        conn = get_connection()
        conn.execute("INSERT INTO minicursos (nome) VALUES (?)", (minicurso.nome,))
        conn.commit()
        conn.close()

    def atualizar(self, minicurso):
        conn = get_connection()
        conn.execute("UPDATE minicursos SET nome = ? WHERE id = ?", (minicurso.nome, minicurso.id))
        conn.commit()
        conn.close()

    def deletar(self, id):
        conn = get_connection()
        conn.execute("DELETE FROM minicursos WHERE id = ?", (id,))
        conn.commit()
        conn.close()