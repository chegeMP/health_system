# app/api.py

from flask import Blueprint, jsonify
from app.models import Client

api = Blueprint('api', __name__)

@api.route('/client/<int:id>', methods=['GET'])
def get_client_profile(id):
    client = Client.query.get_or_404(id)
    programs = [program.name for program in client.programs]

    return jsonify({
        "id": client.id,
        "name": client.name,
        "age": client.age,
        "gender": client.gender,
        "programs": programs
    })
