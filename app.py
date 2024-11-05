from flask import Flask
from rotas import bp  # Importa o Blueprint

app = Flask(__name__)

# Registra o Blueprint na aplicação Flask
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)
