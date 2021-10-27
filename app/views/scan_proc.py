from flask import render_template
from werkzeug.wrappers import request
from app import app

scan_setup_html = "scan/setup.html"

@app.route("/scan/setup",methods =["GET"])
def scan_setup():
   if request.method == "GET":
      return render_template(scan_setup_html)
