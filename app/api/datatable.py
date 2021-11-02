from flask import json, jsonify,request
from app import app
from uuid import uuid1

@app.route("/api/datatable/<table_name>",methods =["GET"])
def datatable_get_table(table_name):
    scan_step_table_json_data={
        "table_name":table_name,
        "data":[]
    }
    for i in range(40):
        scan_step_table_json_data["data"].append(
            {
                "id": i,
                "order" : i+1,
                "command" : "command "+str(i),
                "short_name" : ["short_name" + str(i),123],
                "description" : "description"+str(i),
                "sub_command": True if (i%2 == 0)  else False
            }
        )
    print({"table_name":table_name,})
    return jsonify(**scan_step_table_json_data)

@app.route("/api/datatable/fk/<table_name>/<column_name>/<fk_value>",methods = ["GET"])
def datatable_fk_data(table_name,column_name,fk_value):
    scan_step_table_json_data={
        "table_name":table_name,
        "data":[]
    }
    for i in range(40):
        scan_step_table_json_data["data"].append(
            {
                "id": i,
                "order" : i+1,
                "command" : fk_value,
                "short_name" : ["short_name" + str(i),123],
                "description" : column_name,
                "sub_command": True if (i%2 == 0)  else False
            }
        )
    print({"table_name":table_name,})
    return jsonify(**scan_step_table_json_data)

@app.route("/api/datatable/<table_name>",methods =["POST"])
def datatable_post_table(table_name):
    print("table_name : "+table_name)
    print(request.form.to_dict())
    return jsonify(**request.form.to_dict)

@app.route("/api/datatable/<table_name>/<row_id>",methods =["DELETE"])
def datatable_delete_table(table_name,row_id):
    print("table_name : ",table_name)
    print("id : ",row_id)
    return jsonify(**request.form.to_dict)

@app.route("/api/datatable/swap/<table_name>",methods=["POST"])
def datatable_swap_column(table_name):
    print("table_name : ",table_name)
    print(request.form.to_dict())
    return jsonify(**request.form.to_dict)