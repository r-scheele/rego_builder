from fastapi import Depends, FastAPI, HTTPException
from starlette.responses import RedirectResponse
from app.config.config import settings
from app.database.policy_database import PolicyDatabase, get_db
from app.schemas.rules import RequestObject, UpdateRequestObject
from app.utils.write_rego import delete_policy_file, write_to_file
import os
from app.server.login import router as auth_router

default_path = settings.BASE_PATH


def init_dir() -> None:
    if not os.path.exists(default_path):
        os.mkdir(default_path)


init_dir()

app = FastAPI()
app.include_router(auth_router)


@app.post("/policies/")
async def write_policy(rego_rule: RequestObject, database=Depends(get_db)) -> dict:

    rego_rule = rego_rule.dict()
    database.add_policy(rego_rule)
    write_to_file(rego_rule, operation="write")

    return {"status": 200, "message": "Policy created successfully"}


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
