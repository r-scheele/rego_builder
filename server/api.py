from fastapi import FastAPI
from schemas.rules import RequestObject
from utils.write_rego import write_to_file

app = FastAPI()


@app.post("/save")
async def write(rego_rule: RequestObject) -> dict:
    response = write_to_file(rego_rule)

    response["state"] = rego_rule
    return response


@app.put("/save")
async def modify(rego_rule: RequestObject):
    pass