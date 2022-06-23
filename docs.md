## Full documentation of the API





Table of Contents
=================

* [Introduction](#introduction)
* [Features](#features)
* [How the policy manager works](#architecture)
* [Installation](#installation)
* [How the traslation from JSON to REGO is done](#translation)
* [Usage](#usage)
1. [Input_props_equals](#1-input_props_equals)
   * [Handling * as the wildcard flag](#Handling-'*'-as-the-wildcard-flag)
   * [Allowing all path parameter after a path section, except one](#Handling-'*'-as-the-wildcard-flag)
   * [ Handling equality check between a particular property on the request object and a valueHandling * as the wildcard flag](#Handling-'*'-as-the-wildcard-flag)
   * [Allow access to a particular path](#allow-access-to-a-particular-path)
2. [Input_props_in](#input_props_in)
3. [Input_props_in_as](#input_props_in_as)
4. [allow_full_access](#allow_full_access)
* [API CRUD operations](#api-crud-operations)





Introduction
============
This API is responsible for converting JSON variables to REGO which in turn is used in application policy management. The policy management application is born from the need to manage Open Policy Agent ( OPA ) policies written in REGO from a user interface for non-technical users and an API through JSON for technical users.

Features
============
- Translating JSON to REGO
- CRUD operations for policies for persistence.
- Supports existing policies for editing.

Architecture
============
The architecture of the API is based on the following principles:
- The API is written in Python and FastAPI framework.
- The API is written in a way that it is easy to use, extend, test and maintain.

![Screenshot 2022-06-13 at 09 55 43](https://user-images.githubusercontent.com/67229938/173343113-d51d72b4-84c8-4c3b-8555-af41e59cd2de.png)

View the Architecture in the browser [Here](https://www.figma.com/file/684S7kO4dPQbbZFZr6xZOn/Rego-builder?node-id=0%3A1) 



Installation
============
There are quite a few ways to install the API, each of which are described below:
### - Manual installation 
- Create a virtual environment and install the application dependencies:

```console
$ poetry shell && poetry install
```

- Configure your environment variables:

```dotenv
BASE_PATH = /tmp/fastgeoapi
DATABASE_PATH = /tmp/fastgeoapi/database.json
GITHUB_ACCESS_TOKEN=`cat ~/.github_access_token`
GITHUB_USERNAME=<your_github_username>
GITHUB_URL=<your_github_url where the authorization code lives>
CLIENT_ID=<your_github_client_id>
CLIENT_SECRET=<your_github_client_secret>
SECRET_KEY=<your_secret_key>
ALGORITHM=<your_algorithm e.g HS256>
ENVIRONMENT=<your_environment e.g. production|development>
```

- Run the application from the entry point:

```console
$ python3 main.py
```
- Open [localhost:8000/docs](localhost:8000/docs) for API Documentation

### - Build the application image and start the container -
```console
$ Configure environment variables - the .env file
$ docker-compose -f docker-compose.dev.yml up -d

```
### - Pull the official image from Docker Hub and start the container 

```console
$ docker pull rscheele3214/rego-builder:latest
$ docker run rscheele3214/rego-builder:latest
```


Translation from JSON to REGO.
============
The REGO policies are created by a set of functions called **commands** that serves as the translation logic. Each of these commands is responsible for writing a specific REGO rule to a `.rego` file. However, the JSON to REGO conversion must follow certain conditions as defined by a pydantic model for effectiveness. 
The following is how a rule is defined. The  Policy object which is the request body, as well as the Rule object is pydantic models.

```py3
class Policy:
name: str
rules: List[List[Rule]]
```
Rule Object: <br />
```py3
class Rule(BaseModel):
command: str
properties: Dict[str, Union[str, List[str], Dict[str, Union[str, List[str]]]]]
```

A rule is defined by two keys: command and properties. The command key holds one of the recognized commands and the properties key, holds another dictionary containing the input to the command function e.g `input_property` and `value`. in special cases, the `datasource_item` items are also included in the properties key.

```json     
{
"command": "input_prop_equals",
"properties": {
   "input_property": "request_method",
   "value": "GET"
}
}
```
In the example above, the command key represents the operation to be performed and the properties key represents the properties that are being used in the operation.

`input_prop_equals` is the command in the example that initiates the appropriate operation, on the properties object.
The above rule translates to an equality check between the input property `input_property` and the value `value`. <br /> <br />
The REGO equivalent of the above rule object is: <br />
```rego
`input.request_method == "GET"`
```

Each Rule object forms a specific rule in a Allow block, and a list of Rules forms a Allow block. <br />
```py3
List[Rule] == Allow {
...
}
```

The API supports the following commands; input_prop_equals, input_prop_in, input_prop_in_as, allow_full_access.

Usage
============

This section contains detailed explanations of the commands and examples on how they're used within the API.
### input_props_equals
This command has different logic to handle series of equality checks.
- Handling '*' as the wildcard flag: <br /> 

This logic handles all the paths after a particular section. if `/collections/` is supplied as the option, all the routes after it will be allowed e.g allow `/collections/obs/`, allow `/collections/test-data/obs/`, allow `/collections/obs/` etc. <br /> 

Example:
```json     
{
   "command": "input_prop_equals",
   "properties": {
      "input_property": "request_path",
      "value": ["v1", "collections", "*"]
   }
}
```
In the json above, the `value` key holds an asterik in the values section, to indicate that the endpoint x is allowed to do y.

The REGO equivalent of the above rule object is: <br />
```rego
input.request_path[0] == "v1"
input.request_path[1] == "collections"
```
- Allowing all path parameter after a path section, except one: <br /> 

This logic handles cases where a particular path parameter is to be exempted, the command matches all other parameters aside the exempted one. e.g allow `/collections/obs/`, allow `/collections/test-data/obs/`, allow `/collections/obs/`. deny `/collections/lakes/`. <br /> 

Example:

```json
{
   "command": "input_prop_equals",
   "properties": {
      "input_property": "request_path",
      "value": ["v1", "collections", "*"],
      "exceptional_value": "obs",
   },
}
```
In the json above, the `value` key holds an asterik in the values section, to indicate that the endpoint x is allowed to do y. The `exceptional_value` key holds the value of the path parameter that is to be exempted.

The REGO equivalent of the above rule object is: <br />
```rego
input.request_path[0] == "v1"
input.request_path[1] == "collections"
input.request_path[2] != "obs"
```

-  Handling equality check between a particular property on the request object and a value: <br />
This logic handles cases where a particular property on the input object is to be checked for equality against a value. 
Example:

```json
{
   "command": "input_prop_equals",
   "properties": {
      "input_property": "company",
      "value": "Geobeyond srl"
}
}
```
In the json above, the `value` key holds the value that is to be checked for equality, while the `input_property` key holds the property that is to be checked in the input object.

The REGO equivalent of the above rule object is: <br />
```rego
input.company == "Geobeyond srl"
```



-  Allow access to a particular path: <br />
This logic handles cases where a specific path is to granted access, if certain property is present on the input object.

Example:
```json
[
{
   "command": "input_prop_equals",
   "properties": {
      "input_property": "request_path",
      "value": ["v1", "collections", "lakes"],
   },
},
   {
   "command": "input_prop_equals",
   "properties": {
      "input_property": "request_path",
      "value": "admin",
   },
}
]
```
In the JSON above, the list of objects indicates a very special `allow` block, that combines two commands. The `input_property` key holds the property that is to be validated before the request to that path is passed. 

The REGO equivalent of the above rule object is: <br />
```rego
allow {
   input.request_path == ["v1", "collections", "lakes", ""]
   input.groupname == "admin"
}
```
### input_props_in
This logic checks if a particular property on the input object is present in a list of values from the database. <br />

Example:

```json
{
"command": "input_prop_in",
"properties": {
   "input_property": "company",
   "datasource_name": "items",
   "datasource_loop_variable": "name"
}
}
```
In the json above, the `input_property` key holds the property that is to be validated before the request to that path is passed. The `datasource_name` key holds the name of the datasource(a list) from the database. The `datasource_loop_variable` key holds the name of the key on each object in the datasource.

The rego rules combine data from the database with the input object, to work out certain conditions. The datasource is the list of values from the database, and the `datasource_loop_variable` is the name of the key on each object in the datasource.

The REGO equivalent of the above rule object is: <br />
```rego
input.company == data.items[i].name
```
### input_props_in_as
This logic checks if the value of two properties on the input object is present on one object in the database <br />

Example:
```json
{
   "command": "input_prop_in_as",
   "properties": {
      "datasource_name": "items",
      "datasource_loop_variables": ["name", "everyone"],
      "input_properties": ["preferred_username", "groupname"]
   }
}
```
In the json above, the resulting REGO code loops over the datasource twice, checking for equality between the values of the input properties, and the values of the datasource loop variables.

The REGO equivalent of the above rule object is: <br />
```rego
some i
data.items[i].name == input.preferred_username
data.items[i].everyone == input.groupname
```


### allow_full_access
This logic allows full access to the resources defined. If the value of the property on the input object has a particular value<br />

Example:
```json
[
   {
      "command": "allow_full_access",
      "properties": {
         "input_property": "groupname",
         "value": "EDITOR_ATAC",
      },
   }
]
```
In the JSON above, the result is an allow block that allows access to the resources defined if the value of the property on the input object has a particular value.

```rego
allow {
   input.groupname == "EDITOR_ATAC"
}
```




POST `/policies/`  Create new policy
============
The POST route takes a request body containing the rules defined according to the schema. It is then, used to build a new policy. The response will be a REGO file written and pushed to GitHub as a newly established remote repository, with the request body conforming to a specified syntax described by the pydantic model `Policy`. <br />

An example request body is: <br />

```json
{
"name": "Example",
"rules": [
   [
      {
      "command": "input_prop_equals",
      "properties": {
         "input_property": "request_path",
         "value": [
            "v1",
            "collections",
            "*"
         ],
         "exceptional_value": "obs"
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
         "command": "allow_full_access",
         "properties": {
            "input_property": "groupname",
            "value": "EDITOR_ATAC"
         }
      }
   ]
]}

```

An example response body is: <br />
```json
{"status": 200, "message": "Policy created successfully"}
```



GET `/policies/` Read all policies  
============
The GET route get all policies that have been created. The response will be a list of all policies that have been created by a certain user, and contains all the associating rules with the policy <br />

An example response body is: <br />
```json
[
   {
      "name": "Example",
      "rules": [
         [
            {
            "command": "input_prop_equals",
            "properties": {
               "input_property": "request_path",
               "value": [
                  "v1",
                  "collections",
                  "*"
               ],
               "exceptional_value": "obs"
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
            "command": "allow_full_access",
            "properties": {
               "input_property": "groupname",
               "value": "EDITOR_ATAC"
            }
         }
      ]
   }
]
```


GET `/policies/{policy_name}` 
============
This route gets a specific policy by it's name. The response will be a policy object conforming to the pydantic model `Policy`. <br />
Example response body: <br />
```json
{
"name": "Example",
"rules": [
   [
      {
         "command": "input_prop_equals",
         "properties": {
            "input_property": "request_path",
            "value": [
               "v1",
               "collections",
               "*"
            ],
            "exceptional_value": "obs"
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
         "command": "allow_full_access",
         "properties": {
            "input_property": "groupname",
            "value": "EDITOR_ATAC"
         }
      }
   ]
]}
```
PUT `/policies/{policy_name}` Update existing policy by name
============
This request method is used to update a specific policy by name. The response will be a policy object conforming to the pydantic model `Policy`. <br />
Example response body: <br />
```json
{"status": 200, "message": "Updated successfully"}
```

DELETE `/policies/policy_name}` Delete existing policy by name
============
This request method is used to delete a specific policy by name
Example response body: <br />
```json
{"status": 200, "message": "Policy deleted successfully"}  
```



