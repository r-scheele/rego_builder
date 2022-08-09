from typing import Dict, List, Optional, Union

from pydantic import BaseModel


class Rule(BaseModel):
    command: str
    properties: Dict[str, Union[str, List[str], Dict[str, Union[str, List[str]]]]]


class RequestObject(BaseModel):
    name: str
    rules: List[List[Rule]]
    owner: Optional[str] = ""
    repo_url: Optional[str] = ""
    repo_id: Optional[int] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Example",
                "repo_url": "https://github.com/r-scheele/opal-policy-example",
                "repo_id": 12345,
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
        }


class UpdateRequestObject(BaseModel):
    name: Optional[str]
    rules: Optional[List[List[Rule]]]
    owner: Optional[str] = ""
    repo_url: Optional[str] = ""

    class Config:
        schema_extra = {
            "example": {
                "name": "Example",
                "owner": "r-scheele",
                "repo_url": "https://github.com/r-scheele/opal-policy-example",
                "repo_id": 23456,
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
                ],
            }
        }
