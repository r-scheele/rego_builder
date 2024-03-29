from fastapi import APIRouter, Depends, HTTPException

from app.config.config import settings
from app.database.policy_database import PolicyDatabase, get_db
from app.schemas.policy_model import RequestObject, UpdateRequestObject
from app.server.auth.authorize_token import TokenBearer
from app.server.services.gitlab import GitLabOperations
from app.utils.write_rego import WriteRego

default_path = settings.BASE_PATH

router = APIRouter(tags=["Policy Operations"], prefix="/policies")


@router.get("/")
async def get_policies(
    database: PolicyDatabase = Depends(get_db), dependencies=Depends(TokenBearer())
) -> list:
    return database.get_policies(dependencies["login"])


@router.post("/")
async def write_policy(
    provider: str,
    rego_rule: RequestObject,
    database=Depends(get_db),
    dependencies=Depends(TokenBearer()),
) -> dict:
    if provider == "gitlab":
        rego_rule.repo_url = GitLabOperations(
            rego_rule.repo_id, dependencies["token"]
        ).repo_url_from_id()

    rego_rule.owner = dependencies["login"]
    policy = rego_rule.dict()

    if database.exists(rego_rule.name, dependencies["login"]):
        raise HTTPException(status_code=409, detail="Policy already exists")

    policies = database.get_policies(dependencies["login"])
    policies.append(policy)

    # Write the policy to the database after successful push
    if provider == "gitlab":
        WriteRego(
            access_token=dependencies["token"],
            repo_url=rego_rule.repo_url,
            username=dependencies["login"],
            provider=provider,
            repo_id=rego_rule.repo_id,
        ).write_to_file(policies)
        database.add_policy(policy, dependencies["login"])

        return {"status": 200, "message": "Policy created successfully"}

    WriteRego(
        dependencies["token"], policy["repo_url"], dependencies["login"], provider
    ).write_to_file(policies)

    database.add_policy(policy, dependencies["login"])

    return {"status": 200, "message": "Policy created successfully"}


@router.get("/{policy_id}")
async def retrieve_policy(
    policy_id: str, database=Depends(get_db), dependencies=Depends(TokenBearer())
) -> dict:
    stored_policy = database.get_policy(policy_id, dependencies["login"])
    if not stored_policy:
        raise HTTPException(status_code=404, detail="Policy does not exist")

    return stored_policy


@router.put("/{policy_id}")
async def modify_policy(
    provider: str,
    policy_id: str,
    rego_rule: UpdateRequestObject,
    database=Depends(get_db),
    dependencies=Depends(TokenBearer()),
) -> dict:
    user = dependencies["login"]
    if not database.exists(policy_id, user):
        raise HTTPException(status_code=404, detail="Policy not found")

    # Clean out fields which weren't updated.
    rego_rule = {k: v for k, v in rego_rule.dict().items() if v is not None}

    # Update database
    database.update_policy(policy_name=policy_id, policy=rego_rule, owner=user)

    # Retrieve updated policy
    updated_policy = database.get_policy(policy_id, user)

    policies = database.get_policies(user)

    # Rewrite rego file and update Gitlab
    if provider == "gitlab":
        WriteRego(
            access_token=dependencies["token"],
            repo_url=updated_policy["repo_url"],
            username=dependencies["login"],
            provider=provider,
            repo_id=updated_policy["repo_id"],
        ).write_to_file(policies)
        return {"status": 200, "message": "Updated successfully"}

    # Rewrite rego file and update GitHub
    WriteRego(
        dependencies["token"],
        rego_rule["repo_url"],
        dependencies["login"],
        provider,
    ).write_to_file(policies)

    return {"status": 200, "message": "Updated successfully"}


@router.delete("/{policy_id}")
async def remove_policy(
    provider: str,
    policy_id: str,
    repo_url: str,
    database=Depends(get_db),
    dependencies=Depends(TokenBearer()),
) -> dict:
    user = dependencies["login"]
    if not database.exists(policy_id, user):
        raise HTTPException(status_code=404, detail="Policy not found")

    repo_id = database.get_policy(policy_id, user)["repo_id"]
    # Remove policy from database
    database.delete_policy(policy_id, user, repo_url)

    # Update the policy in the rego file
    policies = database.get_policies(owner=user)
    if provider == "gitlab":
        WriteRego(
            access_token=dependencies["token"],
            repo_id=repo_id,
            username=user,
            provider=provider,
            repo_url=repo_url,
        ).write_to_file(policies)
    WriteRego(
        access_token=dependencies["token"],
        repo_id=repo_id,
        username=user,
        provider=provider,
        repo_url=repo_url,
    ).write_to_file(policies)

    return {"status": 200, "message": "Policy deleted successfully."}
