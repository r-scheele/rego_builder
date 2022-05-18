from pydantic import BaseModel
from typing import List, Tuple, Union, Dict


# Example schemas for properties
input_prop_in_as_example = {
    "datasource_name": "items",
    "datasource_loop_variables": [
        "name",
        "everyone",
    ],
    "input_properties": [
        "preferred_username",
        "groupname",
    ],
}

input_prop_equals = {
    "input_property": "request_path",
    "value": ["v1", "collections", "*"],
}

input_prop_in = {
    "input_property": "company",
    "datasource_name": "items",
    "datasource_loop_variable": "name",
}


class Rule(BaseModel):
    command: str
    properties: Dict[str, Union[str, List[str], Dict[str, Union[str, List[str]]]]]


class RequestObject(BaseModel):
    name: str
    rules: List[List[Rule]]
