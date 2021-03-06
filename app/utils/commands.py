import json


def input_prop_equals(properties) -> str:
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


def input_prop_in(properties) -> str:
    """
    Allow if the 'key on the request' is present as a 'key in any of the objects' in the database(data)

    :param key: request key
    :param value: request value
    :return:
    """
    # Single check in the database
    return f"input.{properties['input_property']} == data.{properties['datasource_name']}[i].{properties['datasource_loop_variable']}"


def input_prop_in_as(properties) -> str:
    """
    Allow if the 'key on the request' is present as a 'key in any of the objects' in the database(data)
    as a particular value

    :param key: request key
    :param value: request value
    :return:
    """
    # Multiple checks in the database
    return f"some i \n  data.{properties['datasource_name']}[i].{properties['datasource_loop_variables'][0]} == input.{properties['data_input_properties'][0]} \n  data.{properties['datasource_name']}[i].{properties['datasource_loop_variables'][1]} == input.{properties['data_input_properties'][1]}"


def allow_full_access(properties) -> str:
    """
    Allow full access to the API, if a property is present on the request

    :return: allow {
        input.preferred_username == "admin"
    }
    """
    return f"input.{properties['input_property']} == " + f'"{properties["value"]}"'
