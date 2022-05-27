from app.database.policy_database import PolicyDatabase, get_db

from app.config.config import settings
from app.schemas.rules import RequestObject
from app.schemas.rules import UpdateRequestObject
from app.utils.write_rego import delete_policy_file
from app.utils.write_rego import write_to_file
from fastapi import FastAPI, Depends, HTTPException
from fastapi import HTTPException

app = FastAPI()

database = PolicyDatabase(settings.DATABASE_PATH)


@app.post("/policy/")
async def write_policy(rego_rule: RequestObject, database=Depends(get_db)) -> dict:

    response = write_to_file(rego_rule)

    if response["status"] == "success":
        database.add_policy(rego_rule)
        response["state"] = rego_rule
        return {"status": 200, "message": "Policy created successfully"}
    else:
        raise HTTPException(status_code=400, detail=response["message"])


@app.get("/policy/{policy}")
async def retrieve_policy(policy: str, database=Depends(get_db)) -> dict:
    stored_policy = database.get_policy(policy)
    return stored_policy


@app.put("/policy/{policy}")
async def modify_policy(
    policy: str, rego_rule: UpdateRequestObject, database=Depends(get_db)
) -> dict:
    if not database.exists(policy):
        raise HTTPException(status_code=404, detail="Policy not found")

    # Clean out fields which weren't updated.
    rego_rule = {k: v for k, v in rego_rule.dict().items() if v is not None}

    # Update database
    database.update_policy(policy, rego_rule)

    # Retrieve updated policy
    updated_policy = database.get_policy(policy)

    # Rewrite rego file and update GitHub
    write_to_file(RequestObject(**updated_policy))

    return {"status": 200, "message": "Updated successfully"}


@app.delete("/policy/{policy}")
async def remove_policy(policy: str, database=Depends(get_db)) -> dict:
    # Remove policy from database
    database.delete_policy(policy)

    # Delete file from path
    delete_policy_file()

    return {"status": 200, "message": "Policy deleted successfully."}
