example_data1 = {
    "name": "Example",
    "rules": [
        [
            {
                "command": "input_prop_equals",
                "properties": ["request_method", "GET"],
            },
            {
                "command": "input_prop_equals",
                "properties": ["request_path", ["v1", "collections", "obs"]],
            },
            {
                "command": "input_prop_equals",
                "properties": ["preferred_username", "dev9ine"],
            },
            {
                "command": "input_prop_in",
                "properties": {
                    "input_property": "company",
                    "datasource_name": "items",
                    "datasource_loop_variable": "name",
                },
            },
        ],
        [
            {
                "command": "input_prop_equals",
                "properties": ["request_path", ["v1"]],
            },
            {
                "command": "input_prop_equals",
                "properties": ["groupname", "VIEWER"],
            },
        ],
        [
            {
                "command": "input_prop_equals",
                "properties": ["request_path", ["v1", "collections", ""]],
            },
            {
                "command": "input_prop_equals",
                "properties": ["groupname", "GEOCITY_ADMINS"],
            },
        ],
    ],
}


example_data2 = {
    "name": "Example2",
    "rules": [
        [
            {
                "command": "input_prop_equals",
                "properties": {
                    "input_property": "request_path",
                    "value": ["v1", "collections", "*"],
                },
            },
            {
                "command": "input_prop_in",
                "properties": {
                    "input_property": "company",
                    "datasource_name": "items",
                    "datasource_loop_variable": "name",
                },
            },
            {
                "command": "input_prop_equals",
                "properties": {
                    "input_property": "request_method",
                    "value": "GET",
                },
            },
        ],
        [
            {
                "command": "input_prop_equals",
                "properties": {
                    "input_property": "request_path",
                    "value": ["v1", "collections"],
                },
            },
            {
                "command": "input_prop_equals",
                "properties": {
                    "input_property": "request_path",
                    "value": ["v1", "collections", "lakes"],
                },
            },
        ],
        [
            {
                "command": "input_prop_equals",
                "properties": {
                    "input_property": "request_path",
                    "value": ["v1", "collections", "*"],
                },
            },
            {
                "command": "input_prop_equals",
                "properties": {
                    "input_property": "company",
                    "value": "geobeyond",
                },
            },
            {
                "command": "input_prop_in_as",
                "properties": {
                    "datasource_name": "items",
                    "datasource_loop_variables": [
                        "name",
                        "everyone",
                    ],
                    "input_properties": [
                        "preferred_username",
                        "groupname",
                    ],
                },
            },
        ],
    ],
}
