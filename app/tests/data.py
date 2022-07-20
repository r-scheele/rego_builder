test_request_object = {
    "name": "Example",
    "owner": "r-scheele",
    "repo_url": "https://github.com/r-scheele/opal-policy-example",
    "rules": [
        [
            {
                "command": "input_prop_equals",
                "properties": {
                    "input_property": "request_path",
                    "value": ["v1", "collections", "*"],
                    "exceptional_value": "obs",
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
                    "value": ["v1", "collections", "obs", "*"],
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
                    "datasource_loop_variables": ["name", "groupname"],
                    "data_input_properties": [
                        "preferred_username",
                        "groupname",
                    ],
                },
            },
        ],
        [
            {
                "command": "allow_full_access",
                "properties": {
                    "input_property": "groupname",
                    "value": "EDITOR_ATAC",
                },
            }
        ],
        [
            {
                "command": "input_prop_equals",
                "properties": {
                    "input_property": "groupname",
                    "value": ["v1", "collections", "test-data"],
                },
            },
            {
                "command": "allow_full_access",
                "properties": {
                    "input_property": "name",
                    "value": "admin",
                },
            },
        ],
        [
            {
                "command": "input_prop_equals",
                "properties": {
                    "input_property": "request_path",
                    "value": ["v1", "collections", "lakes"],
                },
            },
            {
                "command": "allow_full_access",
                "properties": {
                    "input_property": "groupname",
                    "value": "admin",
                },
            },
        ],
    ],
}
