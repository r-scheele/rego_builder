from .map_commands import commands_map


def build_rego(data) -> str:
    """
    Maps each rule object to the corresponding function and builds the rego file

    param: policy object
    return string: rules, to be written to the rego file
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
