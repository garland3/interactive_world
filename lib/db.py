from flask_sqlalchemy import SQLAlchemy


import datetime
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

from pathlib import Path

db = SQLAlchemy()
# https://stackoverflow.com/questions/9692962/flask-sqlalchemy-import-context-issue

class dbwrapper():
    @staticmethod
    def setdb(app):
        db.init_app(app)
        dbwrapper.db = db

    @staticmethod
    def getdb():
        return dbwrapper.db

    @staticmethod
    def setroot(root):
        dbwrapper.rootpath = root
        
    @staticmethod
    def SetupDb():
        p= Path("./maindb.sqlite3")
        if p.exists() is False:
            db.create_all()
            a = imagefile("test.png")
            dbwrapper.db.session.add(a)
            dbwrapper.db.session.commit()


class imagefile(db.Model):
   id = db.Column('image_id', db.Integer, primary_key = True)
   path = db.Column(db.String(200))
   uploaddate =  Column(DateTime, default=func.now()) 

   def __init__(self, path):
        self.path = path

