from flask import Blueprint, render_template, request, redirect, url_for
from dao.inscrito_dao import InscritoDAO
from dao.minicurso_dao import MinicursoDAO
from models.inscrito import Inscrito

# Blueprint de inscritos - responsável por lidar com as rotas relacionadas a inscrições, interagindo com o InscritoDAO, MinicursoDAO e as views correspondentes
inscrito_blueprint = Blueprint('inscritos', __name__, template_folder='templates')

# Instâncias dos DAOs utilizados pelas rotas deste Blueprint
inscrito_dao = InscritoDAO()
minicurso_dao = MinicursoDAO()

# Rota principal: exibe o formulário de inscrição com a lista de minicursos disponíveis carregada dinamicamente do banco
@inscrito_blueprint.route("/")
def index():
    cursos = minicurso_dao.listar_todos()
    return render_template("index.html", minicursos=cursos)

# Rota de inscrição: recebe os dados do formulário via POST, valida os campos e salva o novo inscrito no banco
@inscrito_blueprint.route("/inscrever", methods=["POST"])
def inscrever():
    nome = request.form.get("nome")
    minicurso_id = request.form.get("minicurso_id")

    # Validação dos campos obrigatórios antes de prosseguir com o salvamento
    if not nome:
        return render_template("erro.html", mensagem="Incluir nome!")
    if not minicurso_id:
        return render_template("erro.html", mensagem="Selecione um minicurso válido!")

    novo_inscrito = Inscrito(nome=nome, minicurso_id=minicurso_id)
    inscrito_dao.salvar(novo_inscrito)
    return render_template("sucesso.html")

# Rota de listagem: busca todos os inscritos no banco e os exibe na view correspondente
@inscrito_blueprint.route("/inscritos")
def listar_inscritos():
    lista = inscrito_dao.listar_todos()
    return render_template("inscritos.html", inscritos=lista)

# Rota de exclusão: recebe o ID do inscrito via POST e o remove do banco, redirecionando para a listagem
@inscrito_blueprint.route("/excluir", methods=["POST"])
def excluir():
    id = request.form.get("id")
    inscrito_dao.deletar(id)
    return redirect(url_for('inscritos.listar_inscritos'))