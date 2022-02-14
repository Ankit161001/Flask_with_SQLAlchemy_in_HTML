from flask import Flask, redirect, url_for, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='static/templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id",db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


@app.route("/")
def home():
    #return "Hello! <h1>Nice to meet you!</h1>"
    return render_template("home.html")

@app.route("/registration", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        password = request.form["password"]
        db.session.add(users(first_name = firstname, last_name = lastname, email = email, password = password))
        db.session.commit()
        return f"<h3>Thank you for registering "+firstname+ "!!</h3>"
    else:
        return render_template("registration.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email1 = request.form["t1"]
        password1 = request.form["t2"]
        found_user = users.query.filter_by(email = email1).first()
        if found_user:
            if found_user.password == password1:
                return f"<h3>Logged in successfully</h3>"
            else:
                return f"<h3>User not found</h3>"
        else:
            return f"<h3>User not found</h3>"
    else:
        #return "Hello! <h1>Nice to meet you!</h1>"
        return render_template("login.html")

@app.route("/catalogue")
def catalogue():
    #return "Hello! <h1>Nice to meet you!</h1>"
    return render_template("catalogue.html")

@app.route("/cse")
def cse():
    #return "Hello! <h1>Nice to meet you!</h1>"
    return render_template("cse.html")

@app.route("/eee")
def eee():
    #return "Hello! <h1>Nice to meet you!</h1>"
    return render_template("eee.html")

@app.route("/ece")
def ece():
    #return "Hello! <h1>Nice to meet you!</h1>"
    return render_template("ece.html")

@app.route("/mech")
def mech():
    #return "Hello! <h1>Nice to meet you!</h1>"
    return render_template("mech.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

@app.route("/hehe")
def hello():
    return render_template("hello.html")

@app.route("/view")
def view():
    return render_template("view.html", values = users.query.all())

if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)
