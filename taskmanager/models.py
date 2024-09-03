from taskmanager import db


# category table
class Category(db.Model):
    # schema for category table
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String, unique=True, nullable=False)
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)

    # string representation of category name
    def __repr__(self):
        return self.category_name

# task table
class Task(db.Model):
    # Schema for task table
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String, unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, nullable=False, default=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    # string representation of task name
    def __repr__(self):
        return f"#{self.id} - Task: {self.task_name} | Urgent: {self.is_urgent}"
