from flask import render_template
from app import app

scan_setup_html = "scan/setup.html"

@app.route("/scan/setup")
def scan_setup():
   return render_template(scan_setup_html)
