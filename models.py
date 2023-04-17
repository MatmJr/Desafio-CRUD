from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class EmployeeModel(db.Model):
    __tablename__ = "table"

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer(), unique=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    position = db.Column(db.String(80))
    adress = db.Column(db.String(160))

    def __init__(self, employee_id, name, age, position, adress):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.position = position
        self.adress = adress

    def __repr__(self):
        return f"{self.name}:{self.employee_id}"
