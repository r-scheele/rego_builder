from fastapi import FastAPI, HTTPException

from app.database.policy_database import add_policy, update_policy, exists, get_policy, delete_policy
from app.schemas.rules import RequestObject, UpdateRequestObject
from app.utils.write_rego import write_to_file, delete_policy_file

app = FastAPI()


@app.post("/policy/")
async def write_policy(rego_rule: RequestObject) -> dict:
    add_policy(rego_rule)
    response = write_to_file(rego_rule)

    response["state"] = rego_rule
    return {
        "status": 200,
        "message": "Policy created successfully"
    }


@app.get("/policy/{policy}")
async def retrieve_policy(policy: str) -> dict:
    stored_policy = get_policy(policy)
    return stored_policy


@app.put("/policy/{policy}")
async def modify_policy(policy: str, rego_rule: UpdateRequestObject) -> dict:
    if not exists(policy):
        raise HTTPException(
            status_code=404,
            detail="Policy not found"
        )

    # Clean out fields which weren't updated.
    rego_rule = {k: v for k, v in rego_rule.dict().items() if v is not None}

    # Update database
    update_policy(policy, rego_rule)

    # Retrieve updated policy
    updated_policy = get_policy(policy)

    # Rewrite rego file and update GitHub
    write_to_file(RequestObject(**updated_policy))

    return {
        "status": 200,
        "message": "Updated successfully"
    }


@app.delete("/policy/{policy}")
async def remove_policy(policy: str) -> dict:
    # Remove policy from database
    delete_policy(policy)

    # Delete file from path
    delete_policy_file()

    return {
        "status": 200,
        "message": "Policy deleted successfully."
    }