from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(2000), nullable = False)
    done = db.Column(db.Boolean, default = False, nullable = False)

    __tablename__ = 'todos'