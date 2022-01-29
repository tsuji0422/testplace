from flaskr import app
from flask import redirect, render_template, request, url_for
import sqlite3
DATABASE = "database.db"

@app.route("/")
def index():
    con = sqlite3.connect(DATABASE)
    db_timeLogs = con.execute("SELECT * FROM timeLogs").fetchall()
    con.close()

    timeLogs = []
    for row in db_timeLogs:
        timeLogs.append({"ID": row[0], "date": row[1], "time": row[2]})

    return render_template(
        "index.html",
        timeLogs = timeLogs
    )

@app.route("/form")
def form():
    return render_template(
        "form.html"
    )

@app.route("/register", methods=["POST"])
def register():
    ID = request.form["ID"]
    date = request.form["date"]
    time = request.form["time"]

    con = sqlite3.connect(DATABASE)
    con.execute("INSERT INTO timeLogs VALUES(?, ?, ?)",
                [ID, date, time])
    con.commit()
    con.close()

    return redirect(url_for("index"))