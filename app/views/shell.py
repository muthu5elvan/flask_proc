from flask import render_template,request
from app import app

shell_log_html = "shell/log.html"
shell_result_html = "shell/shell_result.html"

@app.route("/shell/log",methods =["GET"])
def shell_log():
   return render_template(shell_log_html)

@app.route("/shell/result",methods =["GET"])
def shell_result():
   return render_template(shell_result_html)