from flask import jsonify,request
from flask import json
from app import TOASTR_DANGER, TOASTR_INFO, app
from uuid import uuid1


# 
# update the particular cell in the table
# 
"""
Example 
URL : /api/x_editable/<table_name>
Post Data : {'table_name': 'parentTable', 'column_name': 'description', 'pk': '0', 'cell_value': 'description1s'}
"""
@app.route("/api/x_editable/<table_name>",methods=["POST"])
def x_editable_cell_update(table_name):
    req_json = request.get_json()
    cell_data ={}
    cell_data["table_name"]=table_name
    cell_data["column_name"]= req_json["name"]
    cell_data["pk"]=req_json["pk"]
    cell_data["cell_value"]=req_json["value"]
    print(cell_data)

    cell_data["__msg"]={}
    cell_data["__msg"]["color"] = TOASTR_DANGER
    cell_data["__msg"]["heading"] =  "Column Value updated"
    cell_data["__msg"]["text"] = "Value updated successfully"
    return jsonify(**cell_data)