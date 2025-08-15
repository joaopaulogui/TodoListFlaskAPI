import os
from flask import Flask
from models.config import Config
from controllers.todo_controller import UserController
from models.entitiestodo import db
from models.createdb import createDB

createDB();

TodoApp = Flask(__name__)
TodoApp.config.from_object(Config)

#inicializando banco de dados
db.init_app(TodoApp)

#criando as tabelas
with TodoApp.app_context():
    db.create_all()


TodoApp.add_url_rule('/','index', UserController.index)
TodoApp.add_url_rule('/addtodos', 'addtodos', UserController.addtodo, methods = ['GET', 'POST'])

if __name__ == "__main__":
    TodoApp.run()

