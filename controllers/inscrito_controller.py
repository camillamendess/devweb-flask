from flask import Blueprint, render_template, request, redirect, url_for
from dao.inscrito_dao import InscritoDAO
from dao.minicurso_dao import MinicursoDAO
from models.inscrito import Inscrito

inscrito_blueprint = Blueprint('inscritos', __name__, template_folder='templates')
inscrito_dao = InscritoDAO()
minicurso_dao = MinicursoDAO()

@inscrito_blueprint.route("/")
def index():
    # Puxa dinamicamente os cursos salvos no banco para carregar no select
    cursos = minicurso_dao.listar_todos()
    return render_template("index.html", minicursos=cursos)

@inscrito_blueprint.route("/inscrever", methods=["POST"])
def inscrever():
    nome = request.form.get("nome")
    minicurso_id = request.form.get("minicurso_id")

    # 🛡️ SEGURANÇA E VALIDAÇÃO
    if not nome:
        return render_template("erro.html", mensagem="Incluir nome!")
    if not minicurso_id:
        return render_template("erro.html", mensagem="Selecione um minicurso válido!")

    novo_inscrito = Inscrito(nome=nome, minicurso_id=minicurso_id)
    inscrito_dao.salvar(novo_inscrito)
    return render_template("sucesso.html")

@inscrito_blueprint.route("/inscritos")
def listar_inscritos():
    lista = inscrito_dao.listar_todos()
    return render_template("inscritos.html", inscritos=lista)

@inscrito_blueprint.route("/excluir", methods=["POST"])
def excluir():
    id = request.form.get("id")
    inscrito_dao.deletar(id)
    return redirect(url_for('inscritos.listar_inscritos'))