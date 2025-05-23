# app/routes.py
from flask import render_template, redirect, url_for

from flask import Blueprint, request, jsonify
from app import db
from app.models import Program, Client

main = Blueprint('main', __name__)

@main.route('/create_program', methods=['POST'])
def create_program():
    data = request.get_json()
    program_name = data.get('name')
    program_description = data.get('description', '')

    if not program_name:
        return jsonify({"message": "Program name is required!"}), 400

    if Program.query.filter_by(name=program_name).first():
        return jsonify({"message": "Program already exists!"}), 400

    new_program = Program(name=program_name, description=program_description)
    db.session.add(new_program)
    db.session.commit()
    return jsonify({"message": f"Program {program_name} created!"}), 201

@main.route('/register_client', methods=['POST'])
def register_client():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    gender = data.get('gender')
    email = data.get('email')

    if not name or not age or not gender or not email:
        return jsonify({"message": "Name, age, gender, and email are required!"}), 400

    # Check if email already exists
    if Client.query.filter_by(email=email).first():
        return jsonify({"message": "Email already registered!"}), 400

    new_client = Client(name=name, age=age, gender=gender, email=email)
    db.session.add(new_client)
    db.session.commit()
    return jsonify({"message": f"Client {name} registered!"}), 201


@main.route('/enroll_client_by_name', methods=['POST'])
def enroll_client_by_name():
    data = request.get_json()
    name = data.get('name')
    program_name = data.get('program')

    if not name or not program_name:
        return jsonify({"message": "Name and program are required!"}), 400

    client = Client.query.filter_by(name=name).first()
    if not client:
        return jsonify({"message": f"Client with name {name} not found!"}), 404

    program = Program.query.filter_by(name=program_name).first()
    if not program:
        return jsonify({"message": f"Program {program_name} not found!"}), 404

    # Check if the client is already enrolled
    if program in client.programs:
        return jsonify({"message": "Client already enrolled in this program."}), 400

    # Enroll client in the program
    client.programs.append(program)
    db.session.commit()
    
    return jsonify({"message": f"Client {client.name} successfully enrolled in {program_name}!"}), 200


@main.route('/search_client', methods=['GET'])
def search_client():
    name = request.args.get('name')

    if not name:
        return jsonify({"message": "Please provide a name to search."}), 400

    clients = Client.query.filter(Client.name.ilike(f"%{name}%")).all()

    if not clients:
        return jsonify({"message": "No clients found!"}), 404

    results = []
    for client in clients:
        results.append({
            "id": client.id,
            "name": client.name,
            "age": client.age,
            "gender": client.gender
        })

    return jsonify({"results": results}), 200


@main.route('/view_profile/<int:client_id>', methods=['GET'])
def view_profile(client_id):
    client = Client.query.get_or_404(client_id)
    programs = [program.name for program in client.programs]

    return jsonify({
        "id": client.id,
        "name": client.name,
        "age": client.age,
        "gender": client.gender,
        "programs": programs
    })
@main.route('/api/get_clients', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    return jsonify([{"id": client.id, "name": client.name} for client in clients]), 200

@main.route('/api/get_programs', methods=['GET'])
def get_programs():
    programs = Program.query.all()
    return jsonify([{"id": program.id, "name": program.name} for program in programs]), 200

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile/<int:client_id>')
def profile(client_id):
    return render_template('profile.html', client_id=client_id)
