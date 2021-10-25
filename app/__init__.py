from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.model import name

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__,template_folder='template',static_folder="static")
app.debug = True

###############################################################################################
#    Base database config
###############################################################################################
app.config["SQLALCHEMY_DATABASE_URI"] ='sqlite:///' + os.path.join(basedir,"db" ,"user.sqlite")
app.config["SQLALCHEMY_BINDS"] ={
    name.scan_step : 'sqlite:///' + os.path.join(basedir,"db","scan_step" ,"scan_step.sqlite"),
    }
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
##############################################################################################


from app.model import user
from app.model import scan_step

from app import routes