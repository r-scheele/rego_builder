from json import dumps as json
from fastapi import FastAPI
from .models import RequestObject
from rego_build_api.utils.write_rego import write_to_file
from rego_build_api.example_json import example_data2

app = FastAPI()


res = json(example_data2)
# print(res)


@app.post("/save")
async def write(rego_rule: RequestObject):
    response = write_to_file(rego_rule)

    response["state"] = rego_rule
    return response


@app.put("/save")
async def modify(rego_rule: RequestObject):
    pass


# activate the environment with
## poetry shell
# Start the server with
## uvicorn rego_build_api.server.main:app --reload
