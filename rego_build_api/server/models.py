from pydantic import BaseModel
from typing import List, Tuple, Union, Callable


class Rule(BaseModel):
    command: str
    properties: Union[
        Tuple[str, Union[str, List[str]]],
        Tuple[str, Union[str, List[str]], str],
        Tuple[str, ...],
    ]


class RequestObject(BaseModel):
    name: str
    rules: List[List[Rule]]
