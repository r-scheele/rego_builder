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
                "properties": ["company", "items", "name"],
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
                "properties": ["request_method", "GET"],
            },
            {
                "command": "input_prop_equals",
                "properties": ["request_path", [""]],
            },
        ],
        [
            {
                "command": "input_prop_equals",
                "properties": ["request_method", "GET"],
            },
            {
                "command": "input_prop_equals",
                "properties": ["request_path", ["static", "img"]],
            },
        ],
        [
            {
                "command": "input_prop_equals",
                "properties": ["request_method", "GET"],
            },
            {
                "command": "input_prop_equals",
                "properties": ["request_path", ["static", "css"]],
            },
        ],
        [
            {
                "command": "input_prop_equals",
                "properties": ["request_method", "GET"],
            },
            {
                "command": "input_prop_equals",
                "properties": ["request_path", ["collections"]],
            },
        ],
        [
            {
                "command": "input_prop_equals",
                "properties": ["request_method", "GET"],
            },
            {
                "command": "input_prop_equals",
                "properties": ["request_path", ["collections", "obs"]],
            },
            {
                "command": "input_prop_equals",
                "properties": ["company", "geobeyond"],
            },
            {
                "command": "input_prop_in_as",
                "properties": [
                    "preferred_username",
                    "items",
                    "name",
                    "groupname",
                    "everyone",
                ],
            },
        ],
    ],
}
