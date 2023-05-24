from flask import Flask, render_template, request, redirect, abort
from models import db, EmployeeModel

app = Flask(__name__, template_folder="templates")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


@app.route("/")
def index():
    return render_template("mainpage.html")


@app.route("/data/create", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("createpage.html")

    if request.method == "POST":
        cpf = request.form["cpf"]
        name = request.form["name"]
        age = request.form["age"]
        position = request.form["position"]
        address = request.form["address"]
        employee = EmployeeModel(
            cpf=cpf,
            name=name,
            age=age,
            position=position,
            address=address,
        )
        db.session.add(employee)
        db.session.commit()
        return redirect("/data")


@app.route("/data")
def RetrieveList():
    employees = EmployeeModel.query.all()
    return render_template("datalist.html", employees=employees)


@app.route("/data/<int:id>")
def RetrieveEmployee(id):
    employee = EmployeeModel.query.filter_by(id=id).first()
    if employee:
        return render_template("data.html", employee=employee)
    return f"Employee with id ={id} Doenst exist"


@app.route("/data/<int:id>/update", methods=["GET", "POST"])
def update(id):
    employee = EmployeeModel.query.get(id)
    if not employee:
        return f"Employee with id = {id} does not exist"

    if request.method == "POST":
        employee.cpf = request.form["cpf"]
        employee.name = request.form["name"]
        employee.age = request.form["age"]
        employee.position = request.form["position"]
        employee.address = request.form["address"]
        db.session.commit()
        return redirect(f"/data/{id}")

    return render_template("update.html", employee=employee)


@app.route("/data/<int:id>/delete", methods=["GET", "POST"])
def delete(id):
    employee = EmployeeModel.query.filter_by(id=id).first()
    if request.method == "POST":
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return redirect("/data")
        abort(404)

    return render_template("delete.html")


app.run(host="localhost", port=5000)
