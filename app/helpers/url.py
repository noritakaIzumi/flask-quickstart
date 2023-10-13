from typing import Callable


def get_endpoint_name(function: Callable) -> str:
    # noinspection PyUnresolvedReferences
    return str(function.__module__).split(".")[-1] + "." + function.__name__
