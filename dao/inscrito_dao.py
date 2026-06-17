from database import get_connection
from models.inscrito import Inscrito

# DAO de inscritos - responsável por realizar as operações de acesso ao banco de dados relacionadas aos inscritos
class InscritoDAO:

    # Método que lista todos os inscritos, trazendo também o nome do minicurso associado via JOIN
    def listar_todos(self):
        conn = get_connection()
        # JOIN com a tabela de minicursos para trazer o nome do curso associado a cada inscrito
        cursor = conn.execute("""
            SELECT i.id, i.nome, i.minicurso_id, m.nome as minicurso_nome 
            FROM inscritos i 
            LEFT JOIN minicursos m ON i.minicurso_id = m.id
        """)
        rows = cursor.fetchall()
        conn.close()
        return [Inscrito(row['id'], row['nome'], row['minicurso_id'], row['minicurso_nome']) for row in rows]

    # Método que salva um novo inscrito no banco com seu nome e o ID do minicurso escolhido
    def salvar(self, inscrito):
        conn = get_connection()
        conn.execute("INSERT INTO inscritos (nome, minicurso_id) VALUES (?, ?)", (inscrito.nome, inscrito.minicurso_id))
        conn.commit()
        conn.close()

    # Método que remove um inscrito do banco pelo seu ID
    def deletar(self, id):
        conn = get_connection()
        conn.execute("DELETE FROM inscritos WHERE id = ?", (id,))
        conn.commit()
        conn.close()