from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Flask, session, render_template, redirect, request
from flask_session import Session
import secrets
from helpers import login_required, decrypt_password, encrypt_password

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)


db = SQL("sqlite:///lockr.db")


@app.route("/login" , methods=["GET", "POST"])
def login():

    session.clear()

    if request.method == "POST":
 
        if not request.form.get("username"):
            return render_template("error.html", message="Must provide username")

        elif not request.form.get("password"):
            return render_template("error.html", message="Must provide password")


        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return render_template("error.html",message ="Invalid username and/or password")

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "GET":
        return render_template("register.html")
    
    if request.method == "POST":
        if request.form.get("username") == "":
            return render_template("error.html",message= "Username field cannot be empty")
        
        if request.form.get("password") == "" or request.form.get("confirmation") == "":
            return render_template("error.html", message="Password field cannot be empty")
        
        if request.form.get("confirmation") != request.form.get("password"):
            return render_template("error.html",message= "Passwords dont match")

        username = request.form.get("username")
        password = request.form.get("password")
        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, generate_password_hash(password, method='scrypt', salt_length=16))
        except ValueError:
            return render_template("error.html", message="Username already exists")
        return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    session.clear()

    return redirect("/")

@app.route("/", methods= ["GET", "POST"])
@login_required
def index():
    if request.method == 'GET':
        user_id = session["user_id"]
        vault = db.execute("SELECT * FROM passwords WHERE user_id = ?", user_id)

        for row in vault:
            try:
                row["service_password"] = decrypt_password(row["service_password"])
            except:
                row["service_password"] = "[Decryption Error]"
        return render_template("index.html", vault=vault)

    if request.method == 'POST':
        user_id = session["user_id"]
        website = request.form.get("website")
        username = request.form.get("username")
        password = request.form.get("password")
        
        encrypted_password = encrypt_password(password)
        db.execute("INSERT INTO passwords (user_id, service_name, service_username, service_password) VALUES (?, ?, ?, ?)",user_id, website, username, encrypted_password)

        
        vault = db.execute("SELECT * FROM passwords where user_id = ?", user_id)
        for row in vault:
            try:
                row["service_password"] = decrypt_password(row["service_password"])
            except:
                row["service_password"] = "[Decryption Error]"

        return render_template("index.html", vault=vault)

@app.route("/delete", methods= ["POST"])
def delete():
    id = request.form.get("id")
    user_id = session["user_id"]
    db.execute("DELETE FROM passwords WHERE user_id = ? AND id = ?", user_id, id)
    return redirect("/")

@app.route("/edit", methods=["GET","POST"])
@login_required
def edit():
    if request.method == "POST":
        user_id = session["user_id"]
        id = request.form.get("id")
        website = request.form.get("website")
        username = request.form.get("username")
        password = request.form.get("password")
        encrypted_password = encrypt_password(password)
        db.execute("UPDATE passwords SET service_name = ?, service_username = ?, service_password = ? WHERE   user_id = ? AND id = ?", website, username, encrypted_password, user_id, id)
        return redirect("/")
    if request.method == "GET":
        id =  request.args.get("id")
        user_id = session["user_id"]
        vault = db.execute("SELECT * FROM passwords WHERE user_id = ? AND id = ?", user_id, id)
        vault = vault[0]
        vault["service_password"] = decrypt_password(vault["service_password"])
        return render_template("edit.html", id=id, vault=vault)
    