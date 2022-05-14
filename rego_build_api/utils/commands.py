import json
from typing import Tuple


def input_prop_equals(value: Tuple[str, str]) -> str:
    """
    Allow if the 'key on the request' equals the 'value assigned' to it

    :param key: request key
    :param value: request value
    :return:
    """
    input_prop, main_value = value[0], value[1]
    return f"input.{input_prop} == {json.dumps(main_value)}"


def input_prop_in(value: Tuple[str, ...]) -> str:
    """
    Allow if the 'key on the request' is present as a 'key in any of the objects' in the database(data)

    :param key: request key
    :param value: request value
    :return:
    """

    input_prop, datasource_name, datasource_prop = value[0], value[1], value[2]
    return f"input.{input_prop} == data.{datasource_name}[i].{datasource_prop}"


def input_prop_in_as(value: Tuple[str, ...]) -> str:
    """
    Allow if the 'key on the request' is present as a 'key in any of the objects' in the database(data)
    as a particular value

    :param key: request key
    :param value: request value
    :return:
    """

    input_prop, datasource_name, datasource_prop, main_key, main_value = (
        value[0],
        value[1],
        value[2],
        value[3],
        value[4],
    )
    return f"some i \n  data.{datasource_name}[i].{datasource_prop} == input.{input_prop} && data.{datasource_name}[i].{main_key} == {main_value}"
