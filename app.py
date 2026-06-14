from flask import Flask
from database import init_db
from controllers.inscrito_controller import inscrito_blueprint
from controllers.minicurso_controller import minicurso_blueprint

app = Flask(__name__)

init_db()

# Registra os Controladores (Blueprints) no app principal
app.register_blueprint(inscrito_blueprint)
app.register_blueprint(minicurso_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
    