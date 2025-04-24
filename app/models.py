# app/models.py

from app import db

# Association table for many-to-many relationship between Clients and Programs
client_program = db.Table('client_program',
    db.Column('client_id', db.Integer, db.ForeignKey('clients.id'), primary_key=True),
    db.Column('program_id', db.Integer, db.ForeignKey('programs.id'), primary_key=True)
)

class Program(db.Model):
    __tablename__ = 'programs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    clients = db.relationship('Client', secondary=client_program, back_populates='programs')

    def __repr__(self):
        return f"<Program {self.name}>"

class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)

    programs = db.relationship('Program', secondary=client_program, back_populates='clients')

    def __repr__(self):
        return f"<Client {self.name}>"

