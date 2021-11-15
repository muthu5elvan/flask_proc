def array(name,key) -> dict:
    array_json={
            "label": "",
            "reorder": True,
            "initEmpty": True,
            "addAnotherPosition": "bottom",
            "layoutFixed": False,
            "enableRowGroups": False,
            "tableView": True,
            "key": key,
            "type": "datagrid",
            "input": True,
            "components": [
                {
                    "label": name,
                    "key": key,

                    "tableView": True,
                    "type": "textfield",
                    "input": True,
                    
                    "logic": [
                        {
                            "name": "Edit",
                            "trigger": {
                                "type": "simple",
                                "simple": {
                                    "show": True,
                                    "when": key+".edit",
                                    "eq": "edit"
                                }
                            },
                            "actions": [
                                {
                                    "name": "Edit",
                                    "type": "property",
                                    "property": {
                                        "label": "Disabled",
                                        "value": "disabled",
                                        "type": "boolean"
                                    },
                                    "state": False
                                }
                            ]
                        },
                        {
                            "name": "hide",
                            "trigger": {
                                "type": "simple",
                                "simple": {
                                    "show": True,
                                    "when": key+".edit",
                                    "eq": "hide"
                                }
                            },
                            "actions": [
                                {
                                    "name": "hide",
                                    "type": "property",
                                    "property": {
                                        "label": "Disabled",
                                        "value": "disabled",
                                        "type": "boolean"
                                    },
                                    "state": True
                                }
                            ]
                        }
                    ],
                },
                {
                    "label": "Action",
                    "optionsLabelPosition": "right",
                    "inline": False,
                    "tableView": False,
                    "defaultValue": "edit",
                    "values": [
                        {
                            "label": "Edit",
                            "value": "edit",
                            "shortcut": ""
                        },
                        {
                            "label": "Disable",
                            "value": "hide",
                            "shortcut": ""
                        }
                    ],
                    "persistent": "client-only",
                    "key": "edit",
                    "type": "radio",
                    "input": True
                }
            ]
        }

    return array_json