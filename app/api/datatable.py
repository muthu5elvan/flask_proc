from flask import json, jsonify,request
from app import app
from uuid import uuid1

# 
# Parent table data
# 
"""
Example :
URL Data : /api/datatable/<table_name>
Url : /api/datatable/child_data
Response Data =  {
    "data" : {command: "0", description: "id", id: 39, order: 40, short_name: ["short_name39", 123],…},
    "table_name": "childTable"
    }
"""
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

# 
# child table data
# 
"""
Example 
URL OPTION : /api/datatable/fk/<table_name>/<column_name>/<fk_value>
URL : /api/datatable/fk/childTable/id/0
Get Data : 
Response Data : {
    "data" : {command: "0", description: "id", id: 39, order: 40, short_name: ["short_name39", 123],…},
    "table_name": "childTable"
    }
"""
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

# 
# Insert data into table
# 
@app.route("/api/datatable/<table_name>",methods =["POST"])
def datatable_post_table(table_name):
    print("table_name : "+table_name)
    print(request.form.to_dict())
    return jsonify(**request.get_json())

# 
# Delete row in the table
# 
@app.route("/api/datatable/<table_name>/<pk_id>",methods =["DELETE"])
def datatable_delete_table(table_name,pk_id):
    print("table_name : ",table_name)
    print("id : ",pk_id)
    return jsonify(**request.get_json())

# 
# Swap row in the table
# 
"""
Example 
URL OPTION : /api/datatable/swap/<table_name>
URl : /api/datatable/swap/childtable
Post Data : [
    {'command': 'command 1', 'description': 'description1s', 'id': 1, 'order': 2, 'short_name': ['short_name1', 123], 'sub_command': False},
    {'command': 'command 0', 'description': 'description0', 'id': 0, 'order': 1, 'short_name': ['short_name0', 123], 'sub_command': True}
    ]
Response Data : 
"""
@app.route("/api/datatable/swap/<table_name>",methods=["POST"])
def datatable_swap_column(table_name):
    print("table_name : ",table_name)
    print(request.get_json())

    response_data={}    
    response_data["__msg"]={}
    # response_data["__msg"]["color"] = 
    response_data["__msg"]["heading"] =  "Column Swap "
    response_data["__msg"]["text"] = "Column is Swap and updated"
    return jsonify(response_data)
