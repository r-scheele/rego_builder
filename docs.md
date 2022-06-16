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





  Introduction
============
This API is responsible for converting JSON variables to REGO which in turn is used in application policy management. The policy management application is born from the need to manage Open Policy Agent ( OPA ) policies written in REGO from a user interface for non-technical users and an API through JSON for technical users.

  Features
============
   - Translating JSON to REGO
   - CRUD operations for policies for persistence.
   - Supports existing policies for editing.
   - Supports creating new policies from scratch.

   Architecture
   ============
   The architecture of the API is based on the following principles:
   - The API is written in Python and FastAPI framework.
   - The API is written in a way that it is easy to use, extend, test and maintain.

![Screenshot 2022-06-13 at 09 55 43](https://user-images.githubusercontent.com/67229938/173343113-d51d72b4-84c8-4c3b-8555-af41e59cd2de.png)

View the Architecture in the browser [Here](https://www.figma.com/file/684S7kO4dPQbbZFZr6xZOn/Rego-builder?node-id=0%3A1) 



   Installation
   ============
- Manual installation - Available [Here](https://github.com/r-scheele/rego_builder#readme)

- Build your own image and start the container -
   ```bash
   $ Configure environment variables - the .env file
   $ docker-compose -f docker-compose.dev.yml up -d

   ```
- Pull the official image from Docker Hub - and start the container 

   ```bash
   $ docker pull rscheele3214/rego-builder:latest
   $ docker run rscheele3214/rego-builder:latest
   ```


How the translation from JSON to REGO works?
============
The REGO policies are created by a set of functions that serves as the translation logic, They're called commands. Each of these commands is responsible for writing specific REGO rule to a `.rego` file. However, the JSON to REGO conversion must follow certain conditions as defined by a pydantic model for effectiveness. The following is an example of how a rule is defined:

   ```json     
   {
      "command": "input_prop_equals",
      "properties": {
         "input_property": "request_method",
         "value": "GET"
      }
   }
   ```
In this case, The command key represents the operation to be performed and the properties key represents the properties that are being used in the operation.
`input_prop_equals` is the command in example, which initiates the appropriate operation, on the properties object.
The above rule translates to an equality check between the input_property and the value. <br />
The REGO equivalent of the above rule object is: <br />
   `input.request_method == "GET"`

### As of now, the API supports the following commands:
1. input_prop_equals
2. input_prop_in
3. input_prop_in_as
4. allow_full_access


Usage
============
### Detailed explanation of commands with examples: 


## 1. Input_props_equals
   This command has different logic to handle series of equality checks.
  ### - Handling '*' as the wildcard flag: <br /> 

   This logic handles all the paths after a particular section. if `/collections/` is supplied as the option, all the routes after it will be allowed e.g allow `/collections/obs/`, allow `/collections/test-data/obs/`, allow `/collections/obs/` etc. <br /> 

   Rule is simply written as: <br />
   `allow { 
      input.request_path = /collections/...
   }` <br />  and the rule object is:
   ```json     
   {
      "command": "input_prop_equals",
      "properties": {
         "input_property": "request_path",
         "value": ["v1", "collections", "*"]
      }
   }
   ```
   ### - Allowing all path parameter after a path section, except one: <br /> 

   If a particular path parameter is to be exempted, the command matches all other parameters aside the exempted one. e.g allow `/collections/obs/`, allow `/collections/test-data/obs/`, allow `/collections/obs/`. deny `/collections/lakes/`. <br /> 

   Rule is simply written as: <br />
   `allow {
      input.request_path = /collections/...
   }` <br /> 
   `deny {
      input.request_path = /collections/lakes
   }` <br /> 
   and the rule object is:
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
   ### -  Handling equality check between a particular property on the request object and a value: <br />

   `allow {
      input.company = 'Geobeyond srl'
       }` <br /> 
   and the rule object is:
   ```json
   {
      "command": "input_prop_equals",
      "properties": {
         "input_property": "company",
         "value": "Geobeyond srl"
      }
   }
   ```

 ### -  Allow access to a particular path: <br />
 This command is to allow access to a particular path e.g `/v1/collections/obs` if the property of the request equals certain value<br />

   `allow {
  input.request_path == ["v1", "collections", "lakes", ""] input.groupname == "admin"
}` <br /> 
   and the rule object is:
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
   ## 2. Input_props_in
   This command is to check if a particular property on the request object is in a list of values from the database. <br />

   `allow {
        input.company == data.items[i].name
   }` <br /> 
   and the rule object is:
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
   ## 3. Input_props_in_as
   This command is to check if two properties on the request object is present on the same object in the database <br />


   `allow {
         some i \n
         data.items[i].name == input.preferred_username \n
         data.items[i].everyone == input.groupname 
   }` <br /> 
   and the rule object is:
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


## 4. allow_full_access
   This command is to allow full access to the resource, if the property on the request object has a particular value<br />


   `allow {
  input.groupname == "EDITOR_ATAC"
}
   }` <br /> 
   and the rule object is:
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


