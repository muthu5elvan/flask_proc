from flask import json, jsonify,request
from app import app
from uuid import uuid1

@app.route("/api/scan/setup",methods =["GET","POST"])
def scan_step():
    if request.method == "GET":
        
        scan_step_table_json_data={
            "data":[
            ]
        }
        for i in range(40):
            scan_step_table_json_data["data"].append(
                {
                    "id":uuid1(),
                    "order" : i+1,
                    "command" : uuid1(),
                    "short_name" : uuid1(),
                    "description" : uuid1(),

                }
            )
        return jsonify(**scan_step_table_json_data)
