import os

class Config:
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root:password@127.0.0.1:3306/todolist'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY= os.urandom(24)