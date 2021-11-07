from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_socketio import SocketIO , emit
import logging
import sys

from app.model import name

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__,template_folder='template',static_folder="static")
app.debug = True

app.config['SECRET_KEY'] = 'Vettri_vel_muruga_---->'

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

##############################################################################################
#       Toaster background
##############################################################################################
TOASTR_SUCCESS = "green"
TOASTR_WARNING = "goldenrod"
TOASTR_INFO = "#17a2b8"
TOASTR_DANGER = "red"
##############################################################################################

CORS(app)
socketio = SocketIO(app)

logging.getLogger("werkzeug").setLevel(logging.ERROR)
green = "\033[92m"
end = "\033[0m"

log_format = green + "pyxtermjs > " + end + "%(levelname)s (%(funcName)s:%(lineno)s) %(message)s"


logging.basicConfig(
        format=log_format,
        stream=sys.stdout,
        level=logging.DEBUG,
    )


from app.model import user
from app.model import scan_step
from app.ws.shell import interact
from app import routes