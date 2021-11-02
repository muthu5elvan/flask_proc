from flask import jsonify,request
from flask import json
from app import app
from uuid import uuid1

@app.route("/api/x_editable/<table_name>",methods=["POST"])
def x_editable_cell_update(table_name):
    print(request.form.to_dict())
    cell_data ={}
    cell_data["table_name"]=table_name
    cell_data["column_name"]= request.form.get("name")
    cell_data["pk"]=json.loads(request.form.get("pk"))
    cell_data["cell_value"]=json.loads(request.form.get("value"))
    print(cell_data)
    return jsonify(**cell_data)