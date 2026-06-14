from flask import Blueprint, render_template, request, redirect, url_for
from dao.minicurso_dao import MinicursoDAO
from models.minicurso import Minicurso

minicurso_blueprint = Blueprint('minicursos', __name__, template_folder='templates')
dao = MinicursoDAO()

@minicurso_blueprint.route("/minicursos")
def listar():
    lista = dao.listar_todos()
    return render_template("minicursos/listar.html", minicursos=lista)

@minicurso_blueprint.route("/minicursos/criar", methods=["GET", "POST"])
def criar():
    if request.method == "POST":
        nome = request.form.get("nome")
        if not nome:
            return render_template("erro.html", mensagem="Nome do minicurso é obrigatório!")
        dao.salvar(Minicurso(nome=nome))
        return redirect(url_for('minicursos.listar'))
    return render_template("minicursos/criar.html")

@minicurso_blueprint.route("/minicursos/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    curso = dao.buscar_por_id(id)
    if not curso:
        return render_template("erro.html", mensagem="Minicurso não encontrado!")
    
    if request.method == "POST":
        curso.nome = request.form.get("nome")
        dao.refresh_db_from_model = dao.atualizar(curso)
        return redirect(url_for('minicursos.listar'))
        
    return render_template("minicursos/editar.html", minicurso=curso)

@minicurso_blueprint.route("/minicursos/excluir", methods=["POST"])
def excluir():
    id = request.form.get("id")
    dao.deletar(id)
    return redirect(url_for('minicursos.listar'))