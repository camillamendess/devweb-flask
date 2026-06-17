# Model Inscrito - representa um inscrito na aplicação, mapeando os dados armazenados no banco para um objeto Python
class Inscrito:

    # Construtor: inicializa os atributos do inscrito, incluindo o nome do minicurso associado para facilitar a exibição na listagem
    def __init__(self, id=None, nome=None, minicurso_id=None, minicurso_nome=None):
        self.id = id
        self.nome = nome
        self.minicurso_id = minicurso_id
        self.minicurso_nome = minicurso_nome