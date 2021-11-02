from flask import render_template
from werkzeug.wrappers import request
from app import app

scan_setup_html = "scan/setup.html"

@app.route("/scan/setup",methods =["GET"])
def scan_setup():
   return render_template(scan_setup_html)