from database import get_connection
from models.inscrito import Inscrito

class InscritoDAO:
    def listar_todos(self):
        conn = get_connection()
        # JOIN para trazer o nome correto do curso associado
        cursor = conn.execute("""
            SELECT i.id, i.nome, i.minicurso_id, m.nome as minicurso_nome 
            FROM inscritos i 
            LEFT JOIN minicursos m ON i.minicurso_id = m.id
        """)
        rows = cursor.fetchall()
        conn.close()
        return [Inscrito(row['id'], row['nome'], row['minicurso_id'], row['minicurso_nome']) for row in rows]

    def salvar(self, inscrito):
        conn = get_connection()
        conn.execute("INSERT INTO inscritos (nome, minicurso_id) VALUES (?, ?)", (inscrito.nome, inscrito.minicurso_id))
        conn.commit()
        conn.close()

    def deletar(self, id):
        conn = get_connection()
        conn.execute("DELETE FROM inscritos WHERE id = ?", (id,))
        conn.commit()
        conn.close()