from fastapi import Depends, HTTPException, APIRouter

from app.config.config import settings
from app.database.policy_database import PolicyDatabase, get_db
from app.schemas.rules import RequestObject, UpdateRequestObject
from app.server.auth.authorize import JWTBearer
from app.utils.write_rego import WriteRego

default_path = settings.BASE_PATH

router = APIRouter()


@router.get("/policies")
async def get_policies(
        database: PolicyDatabase = Depends(get_db), dependencies=Depends(JWTBearer())
) -> list:
    return database.get_policies()


@router.post("/policies/")
async def write_policy(
        rego_rule: RequestObject,
        database=Depends(get_db),
        dependencies=Depends(JWTBearer()),
) -> dict:
    rego_rule = rego_rule.dict()
    database.add_policy(rego_rule)
    WriteRego(dependencies).write_to_file(rego_rule, operation="write")

    return {"status": 200, "message": "Policy created successfully"}


@router.get("/policies/{policy_id}")
async def retrieve_policy(
        policy_id: str, database=Depends(get_db), dependencies=Depends(JWTBearer())
) -> dict:
    stored_policy = database.get_policy(policy_id)
    return stored_policy


@router.put("/policies/{policy_id}")
async def modify_policy(
        policy_id: str,
        rego_rule: UpdateRequestObject,
        database=Depends(get_db),
        dependencies=Depends(JWTBearer()),
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
    WriteRego(dependencies).write_to_file(
        updated_policy,
        operation="update",
    )

    return {"status": 200, "message": "Updated successfully"}


@router.delete("/policies/{policy_id}")
async def remove_policy(
        policy_id: str, database=Depends(get_db), dependencies=Depends(JWTBearer())
) -> dict:
    if not database.exists(policy_id):
        raise HTTPException(status_code=404, detail="Policy not found")
    # Remove policy from database
    database.delete_policy(policy_id)

    # Delete file from path
    WriteRego(dependencies).delete_policy_file()

    return {"status": 200, "message": "Policy deleted successfully."}
