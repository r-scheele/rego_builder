# Open Policy API Manager

This API application is responsible for converting JSON variables to REGO which in turn is used in open policy API management.

## Installation

The API application can be installed and run from any of the following methods:

### From GitHub

Start by cloning the repo:

```console
$ git clone https://github.com/r-scheele/rego_builder
```

Next, create a virtual environment and install the application dependencies:

```console
$ poetry shell && poetry install
```

Next, Configure your environment variables:

```dotenv
BASE_PATH = /tmp/fastgeoapi
DATABASE_PATH = /tmp/fastgeoapi/database.json
GITHUB_ACCESS_TOKEN=`cat ~/.github_access_token`
GITHUB_USERNAME=<your_github_username>
GITHUB_URL=<your_github_url where the authorization code lives>
ENVIRONMENT=<your_environment e.g. production|development>
HOST=datasource <production>, HOST=localhost <development>
PORT=5432
DB_USER=postgres
PASSWORD=postgres
DATABASE=datasource
```

Run the application - production mode:



```console
$ gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.server.api:app --bind 0.0.0.0:8080
```

Create a postgres database, called datasource <br />
  
  ```console
  $ psql -U postgres
  postgres=# CREATE DATABASE datasource
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
  ```

Run the application entry point - development mode:



```console
$ uvicorn app.server.api:app --port 8080 --reload
```


Open [localhost:8000/docs](localhost:8000/docs) for API Documentation.

### Deploying from docker-compose

Configure your environment variables as instructed in the section above, then start your container:

```console
$ docker-compose -f docker-compose.dev.yml up -d
```

Open [localhost:8000/docs](localhost:8000/docs) for API Documentation.

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
  input.request_path[0] == "v1"
  input.request_path[1] == "collections"

  input.company == data.items[i].name
  input.request_method == "GET"
}

allow {
  input.request_path == ["v1", "collections"]
  input.request_path == ["v1", "collections", "lakes"]
}

allow {
  input.request_path[0] == "v1"
  input.request_path[1] == "collections"

  input.company == "geobeyond"
  some i
  data.items[i].name == input.preferred_username
  data.items[i].everyone == input.groupname
}
```

## Test

Test the GitHub actions workflow with the following command:

- Change the `DOCKER_HUB_ACCESS_TOKEN` and `DOCKER_HUB_USERNAME` in the job file to your credentials.


- Run the following command in the terminal:

```console
act --container-architecture linux/amd64
```