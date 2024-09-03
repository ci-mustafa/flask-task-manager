from flask import render_template
from . import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("base.html")