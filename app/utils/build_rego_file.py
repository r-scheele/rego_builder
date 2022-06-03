from .commands_map import commands_map


def build_rego(data) -> str:
    """
    Builds the rego file from the data.

    :return: long rego string to write to file
    """
    output = ""
    for rule in data:
        output += "allow {\n"
        for command in rule:
            func = commands_map[command["command"]]
            output += "  " + func(command["properties"]) + "\n"

        if "full_access" in command["command"]:
            output += "}\n\n"
            continue

        output += "}\n\n"

    return output
