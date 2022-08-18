import json


def input_prop_equals(properties: dict) -> str:
    """
    Allow if the 'key on the request' equals the 'value assigned' to it

    :param key: request key
    :param value: request value
    :return:
    """
    paths = properties["value"]
    if "*" in paths and type(paths) == list:
        # Allows all the paths, except the base path, and the exempted path variable
        result = ""
        for index, path_variable in enumerate(paths):

            # Logic that handles the wildcard flag
            result += (
                f'input.{properties["input_property"]}[{index}] == "{path_variable}" \n  '
                if path_variable != "*"
                else ""
            )
        return (
            # Logic that handles the exempted path variable input.request_path[index] != "obs"
            f"{result}"
            + f'\n  input.{properties["input_property"]}[{len(paths)-1}] != "{properties["exceptional_value"]}"'
            if properties.get("exceptional_value")
            else ""
        )
    elif type(paths) == str:
        # Logic that handles equality checks e.g input.company == "geobeyond"
        return f'input.{properties["input_property"]} == "{paths}"'

    else:
        # Logic that handles a unique path input.request_path == ["v1", "collections", "obs", ""]
        paths.append("")
        return f"input.{properties['input_property']} == {json.dumps(paths)}"


def input_prop_in(properties: dict) -> str:
    """
    Allow if the 'key on the request' is present as a 'key in any of the objects' in the database(data)

    :param key: request key
    :param value: request value
    :return:
    """

    # Comparison with value in the database
    return f"input.{properties['input_property']} == data.{properties['datasource_name']}[_].{properties['input_property']}"


def allow_full_access(properties) -> str:
    """
    Allow full access to the API, if a property is present on the request

    :return: allow {
        input.preferred_username == "admin"
    }
    """
    return f"input.{properties['input_property']} == " + f'"{properties["value"]}"'


def allow_if_object_in_database(properties) -> str:
    # Rule object example for this command
    # rule = {
    #     "command": "allow_if_object_in_database",
    #     "properties": {
    #         "datasource_name": "usergroups",
    #         "datasource_variables": ["name", "groupname"],
    #     },
    # }

    """
    Allow if two properties on the input object matches an object in the database
    """
    user = {
        variable: f"input.{variable}" for variable in properties["datasource_variables"]
    }
    obj = "{"
    for key, value in user.items():
        obj += f'"{key}": {value},'
    obj = obj[:-1] + "}"

    return f"{obj} == data.{properties['datasource_name']}[_]"
