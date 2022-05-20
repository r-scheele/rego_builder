from typing import List, Union, Dict

from pydantic import BaseModel

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

    class Config:
        schema_extra = {
            "example": {"name": "Example2", "rules": [[{"command": "input_prop_equals",
                                 "properties": {"input_property": "request_path", "value": ["v1", "collections", "*"]}},
                                {"command": "input_prop_in",
                                 "properties": {"input_property": "company", "datasource_name": "items",
                                                "datasource_loop_variable": "name"}}, {"command": "input_prop_equals",
                                                                                       "properties": {
                                                                                           "input_property": "request_method",
                                                                                           "value": "GET"}}], [
                                   {"command": "input_prop_equals",
                                    "properties": {"input_property": "request_path", "value": ["v1", "collections"]}},
                                   {"command": "input_prop_equals", "properties": {"input_property": "request_path",
                                                                                   "value": ["v1", "collections",
                                                                                             "lakes"]}}], [
                                   {"command": "input_prop_equals", "properties": {"input_property": "request_path",
                                                                                   "value": ["v1", "collections",
                                                                                             "*"]}},
                                   {"command": "input_prop_equals",
                                    "properties": {"input_property": "company", "value": "geobeyond"}},
                                   {"command": "input_prop_in_as", "properties": {"datasource_name": "items",
                                                                                  "datasource_loop_variables": ["name",
                                                                                                                "everyone"],
                                                                                  "input_properties": [
                                                                                      "preferred_username",
                                                                                      "groupname"]}}]]}

        }