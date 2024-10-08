from flask import Blueprint, jsonify

bp = Blueprint('api', __name__)

@bp.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Bienvenue dans l'application de résumé de texte!"})

@bp.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})