# Rego Policy Manager API

## Description

This API is responsible for converting JSON variables to REGO which in turn is used in application policy management.

## Installation

- Create a virtual environment and install the application dependencies:

```console
$ poetry shell
```

- Run the application from the entry point

```console
$ python main.py
```

Open [localhost:8000/docs](localhost:8000/docs) for API Documentation

## Example

An example JSON file converted to REGO is:

```json
{
  "name": "Example2",
  "rules": [
    [
      {
        "command": "input_prop_equals",
        "properties": {
          "input_property": "request_path",
          "value": ["v1", "collections", "*"]
        }
      },
      {
        "command": "input_prop_in",
        "properties": {
          "input_property": "company",
          "datasource_name": "items",
          "datasource_loop_variable": "name"
        }
      },
      {
        "command": "input_prop_equals",
        "properties": {
          "input_property": "request_method",
          "value": "GET"
        }
      }
    ],
    [
      {
        "command": "input_prop_equals",
        "properties": {
          "input_property": "request_path",
          "value": ["v1", "collections"]
        }
      },
      {
        "command": "input_prop_equals",
        "properties": {
          "input_property": "request_path",
          "value": ["v1", "collections", "lakes"]
        }
      }
    ],
    [
      {
        "command": "input_prop_equals",
        "properties": {
          "input_property": "request_path",
          "value": ["v1", "collections", "*"]
        }
      },
      {
        "command": "input_prop_equals",
        "properties": {
          "input_property": "company",
          "value": "geobeyond"
        }
      },
      {
        "command": "input_prop_in_as",
        "properties": {
          "datasource_name": "items",
          "datasource_loop_variables": ["name", "everyone"],
          "input_properties": ["preferred_username", "groupname"]
        }
      }
    ]
  ]
}
```

The application's login in turn converts this to REGO:

```rego
package httpapi.authz
import input
default allow = false



allow {
  input.request_path[0] == 'v1'
  input.request_path[1] == 'collections'

  input.company == data.items[i].name
  input.request_method == "GET"
}

allow {
  input.request_path == ["v1", "collections"]
  input.request_path == ["v1", "collections", "lakes"]
}

allow {
  input.request_path[0] == 'v1'
  input.request_path[1] == 'collections'

  input.company == "geobeyond"
  some i
  data.items[i].name == input.preferred_username
  data.items[i].everyone == groupname
}
```
