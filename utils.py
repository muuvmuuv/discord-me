import ast

from typing import Literal


def bytes_to_dict(byte_str: Literal[str]):
    dict_str = byte_str.decode("UTF-8")
    lit_dict = ast.literal_eval(dict_str)
    return lit_dict
