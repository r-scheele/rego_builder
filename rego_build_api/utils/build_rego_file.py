from typing import Dict, List
from .commands_map import commands_map


def build_rego(data) -> str:
    """
    Builds the rego file from the data.

    :return: long rego string to write to file
    """
    output = ""

    rules = [[line.dict() for line in rule] for rule in data]

    for rule in rules:
        output += "allow {\n"
        for command in rule:
            func = commands_map[command["command"]]
            output += "  " + func(command["properties"]) + "\n"
        output += "}\n\n"

    return output
