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


@app.post("/policies/")
async def write_policy(rego_rule: RequestObject, database=Depends(get_db)) -> dict:

    rego_rule = rego_rule.dict()
    database.add_policy(rego_rule)
    response = write_to_file(rego_rule, operation="write")

    if response["status"] == "success":
        rego_rule["old_state"] = response["old_state"]
        response["state"] = rego_rule
        return {
            "status": 200,
            "message": "Policy created successfully",
            "state": rego_rule,
        }
    else:
        raise HTTPException(status_code=400, detail=response["message"])


@app.get("/policies/{policy_id}")
async def retrieve_policy(policy_id: str, database=Depends(get_db)) -> dict:
    stored_policy = database.get_policy(policy_id)
    return stored_policy


@app.put("/policies/{policy_id}")
async def modify_policy(
    policy_id: str, rego_rule: UpdateRequestObject, database=Depends(get_db)
) -> dict:
    if not database.exists(policy_id):
        raise HTTPException(status_code=404, detail="Policy not found")

    # Clean out fields which weren't updated.
    rego_rule = {k: v for k, v in rego_rule.dict().items() if v is not None}

    # Update database
    database.update_policy(policy_id, rego_rule)

    # Retrieve updated policy
    updated_policy = database.get_policy(policy_id)

    # Rewrite rego file and update GitHub
    write_to_file(
        updated_policy,
        operation="update",
    )

    return {"status": 200, "message": "Updated successfully"}


@app.delete("/policies/{policy_id}")
async def remove_policy(policy_id: str, database=Depends(get_db)) -> dict:
    # Remove policy from database
    database.delete_policy(policy_id)

    # Delete file from path
    delete_policy_file()

    return {"status": 200, "message": "Policy deleted successfully."}
