from flask import render_template, request, session, redirect, flash, url_for
from . import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    tasks = list(Task.query.order_by(Task.task_name).all())
    return render_template("tasks.html", tasks=tasks)

@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category_to_add = request.form.get("category_name")
        category = Category(category_name=category_to_add.title())
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")

@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("update_category.html", category=category)


@app.route("/category_delete_confirm/<int:category_id>")
def category_delete_confirm(category_id):
    category = Category.query.get_or_404(category_id)
    return render_template("category_delete_confirmation.html", category=category)


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        task = Task(
            task_name = request.form.get("task_name").title(),
            task_description = request.form.get("task_description"),
            is_urgent = True if request.form.get("is_urgent") else False,
            due_date = request.form.get("due_date"),
            category_id = request.form.get("category_id")
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_task.html", categories=categories)


@app.route("/edit_task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        task.task_name = request.form.get("task_name")
        task.task_description = request.form.get("task_description")
        task.due_date = request.form.get("due_date")
        task.is_urgent = True if request.form.get("is_urgent") else False
        task.category_id = request.form.get("category_id")
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("update_task.html", categories=categories, task=task)


@app.route("/task_delete_confirm/<int:task_id>")
def task_delete_confirm(task_id):
    task = Task.query.get_or_404(task_id)
    return render_template("task_delete_confirmation.html", task=task)


@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))





