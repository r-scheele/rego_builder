from .commands import (
    allow_full_access,
    input_prop_equals,
    input_prop_in,
    allow_if_object_in_database,
)

commands_map = {
    "input_prop_equals": input_prop_equals,
    "input_prop_in": input_prop_in,
    "allow_full_access": allow_full_access,
    "allow_if_object_in_database": allow_if_object_in_database,
}
