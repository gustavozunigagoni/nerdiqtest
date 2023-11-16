from flask import Blueprint

root = Blueprint('root', __name__)

@root.route('/')
def index():
    return 'Hola al root de nerdiqtest!!!'