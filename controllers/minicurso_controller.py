from flask import Blueprint, render_template, request, redirect, url_for
from dao.minicurso_dao import MinicursoDAO
from models.minicurso import Minicurso

# Blueprint de minicursos - responsável por lidar com as rotas relacionadas a minicursos, interagindo com o MinicursoDAO e as views correspondentes
minicurso_blueprint = Blueprint('minicursos', __name__, template_folder='templates')

# Instância do DAO utilizada pelas rotas deste Blueprint
dao = MinicursoDAO()

# Rota de listagem: busca todos os minicursos no banco e os exibe na view correspondente
@minicurso_blueprint.route("/minicursos")
def listar():
    lista = dao.listar_todos()
    return render_template("minicursos/listar.html", minicursos=lista)

# Rota de criação: exibe o formulário via GET e salva o novo minicurso no banco via POST, validando o campo nome antes de prosseguir
@minicurso_blueprint.route("/minicursos/criar", methods=["GET", "POST"])
def criar():
    if request.method == "POST":
        nome = request.form.get("nome")
        # Validação do campo obrigatório antes de prosseguir com o salvamento
        if not nome:
            return render_template("erro.html", mensagem="Nome do minicurso é obrigatório!")
        dao.salvar(Minicurso(nome=nome))
        return redirect(url_for('minicursos.listar'))
    return render_template("minicursos/criar.html")

# Rota de edição: busca o minicurso pelo ID via GET e atualiza seus dados no banco via POST, redirecionando para a listagem em seguida
@minicurso_blueprint.route("/minicursos/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    # Verifica se o minicurso existe antes de prosseguir com a edição
    curso = dao.buscar_por_id(id)
    if not curso:
        return render_template("erro.html", mensagem="Minicurso não encontrado!")
    
    if request.method == "POST":
        curso.nome = request.form.get("nome")
        dao.refresh_db_from_model = dao.atualizar(curso)
        return redirect(url_for('minicursos.listar'))
        
    return render_template("minicursos/editar.html", minicurso=curso)

# Rota de exclusão: recebe o ID do minicurso via POST e o remove do banco, redirecionando para a listagem
@minicurso_blueprint.route("/minicursos/excluir", methods=["POST"])
def excluir():
    id = request.form.get("id")
    dao.deletar(id)
    return redirect(url_for('minicursos.listar'))