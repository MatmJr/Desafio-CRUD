from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class EmployeeModel(db.Model):
    __tablename__ = "table"

    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11))
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    position = db.Column(db.String(80))
    address = db.Column(db.String(80))

    def __init__(self, cpf, name, age, position, address):
        self.cpf = cpf
        self.name = name
        self.age = age
        self.position = position
        self.address = address

    def __repr__(self):
        return f"{self.name}:{self.id}"

