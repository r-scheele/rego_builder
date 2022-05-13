from fastapi import FastAPI
from .models import RequestObject
from rego_build_api.utils.write_rego import write_to_file


app = FastAPI()


@app.post("/save")
async def root(rego_rule: RequestObject):
    response = write_to_file(rego_rule)
    return {"result": response}


# activate the environment with
## poetry shell
# Start the server with
## uvicorn rego_build_api.server.main:app --reload
