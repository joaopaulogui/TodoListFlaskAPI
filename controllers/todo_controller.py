from flask import render_template, request, redirect, url_for
from models.entitiestodo import Todo, db


class UserController:
    @staticmethod
    def index():
        todos = Todo.query.all()
        return render_template('index.html', todos=todos)
    
    @staticmethod
    def addtodo():
        if request.method == 'POST':
            name = request.form['name']
            desc = request.form['desc']
            new_todo = Todo(name = name, desc = desc)
            db.session.add(new_todo)
            db.session.commit()

            return redirect(url_for('index'))

        return render_template('addtodo.html')