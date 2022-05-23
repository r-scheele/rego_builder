import json


def input_prop_equals(properties) -> str:
    """
    Allow if the 'key on the request' equals the 'value assigned' to it

    :param key: request key
    :param value: request value
    :return:
    """

    if "*" in properties["value"]:
        result = ""
        for index, path_variable in enumerate(properties["value"]):
            result += (
                f"input.{properties['input_property']}[{index}] == '{path_variable}' \n  "
                if path_variable != "*"
                else ""
            )
        return result
    else:
        return (
            f"input.{properties['input_property']} == {json.dumps(properties['value'])}"
        )


def input_prop_in(properties) -> str:
    """
    Allow if the 'key on the request' is present as a 'key in any of the objects' in the database(data)

    :param key: request key
    :param value: request value
    :return:
    """

    return f"input.{properties['input_property']} == data.{properties['datasource_name']}[i].{properties['datasource_loop_variable']}"


def input_prop_in_as(properties) -> str:
    """
    Allow if the 'key on the request' is present as a 'key in any of the objects' in the database(data)
    as a particular value

    :param key: request key
    :param value: request value
    :return:
    """

    return f"some i \n  data.{properties['datasource_name']}[i].{properties['datasource_loop_variables'][0]} == input.{properties['input_properties'][0]} \n  data.{properties['datasource_name']}[i].{properties['datasource_loop_variables'][1]} == {properties['input_properties'][1]}"
