from flask import json, jsonify,request
from app import app
from uuid import uuid1

@app.route("/api/scan/setup",methods =["GET"])
def scan_step_get():
    scan_step_table_json_data={
        "data":[
        ]
    }
    for i in range(40):
        scan_step_table_json_data["data"].append(
            {
                "id": str(i),
                "order" : i+1,
                "command" : "command "+str(i),
                "short_name" : "short_name" + str(i),
                "description" : "description"+str(i),
                "sub_command":False

            }
        )
    return jsonify(**scan_step_table_json_data)

