from typing import List, Dict

from rego_build_api.server.models import RequestObject
from .build_rego_file import build_rego


def write_to_file(rule: RequestObject) -> None:
    with open(f"rego_build_api.{rule.name}.rego", "w") as file:
        result = build_rego(rule.rules)
        file.write(result)
        return {"status": "success"}
