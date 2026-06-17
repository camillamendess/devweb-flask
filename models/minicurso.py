# Model Minicurso - representa um minicurso na aplicação, mapeando os dados armazenados no banco para um objeto Python
class Minicurso:

    # Construtor: inicializa os atributos do minicurso com ID e nome
    def __init__(self, id=None, nome=None):
        self.id = id
        self.nome = nome