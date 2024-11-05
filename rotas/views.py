from flask import Blueprint, render_template

# Define o Blueprint
bp = Blueprint('main', __name__)

# Define a rota usando o Blueprint
@bp.route('/')
def home():
    return render_template('index.html')
