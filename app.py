from flask import Flask
from database import init_db
from controllers.inscrito_controller import inscrito_blueprint
from controllers.minicurso_controller import minicurso_blueprint

# Ponto de entrada da aplicação Flask - inicializa o banco de dados e registra os Blueprints de inscritos e minicursos
app = Flask(__name__)

# Inicializa o banco de dados, criando as tabelas caso ainda não existam
init_db()

# Registra os Blueprints no app principal, ativando as rotas de inscritos e minicursos
app.register_blueprint(inscrito_blueprint)
app.register_blueprint(minicurso_blueprint)

# Inicia o servidor Flask em modo debug quando executado diretamente
if __name__ == '__main__':
    app.run(debug=True)