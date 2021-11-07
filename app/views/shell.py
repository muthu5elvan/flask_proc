from flask import render_template,request
from app import app

shell_log_html = "shell/log.html"
shell_interact_html = "shell/interact.html"

@app.route("/shell/log",methods =["GET"])
def shell_log():
   return render_template(shell_log_html)

@app.route("/shell/interact",methods =["GET"])
def shell_result():
   return render_template(shell_interact_html)