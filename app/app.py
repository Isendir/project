
# *-* coding: utf-8 *-*
__author__ = 'Ampelio Cherubini'
__version__ = '0.1'
from app import app
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import app.models
from app.models import Base


SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
db = SQLAlchemy(app)
db.Model = Base
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@app.route('/')
def hello():
    return render_template('layout.html')

if __name__ == '__main__':
    manager.run()