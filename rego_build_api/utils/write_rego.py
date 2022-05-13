from typing import List, Dict

from rego_build_api.server.models import RequestObject
from .build_rego_file import build_rego

data = {
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
                "properties": ["company", "data", "name"],
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
    ]
}


def write_to_file(rule: RequestObject) -> None:
    with open(f"rego_build_api.{rule.name}.rego", "w") as file:
        result = build_rego(rule.rules)
        file.write(result)
