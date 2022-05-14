from typing import Iterable


def parse_sequence(seq: Iterable) -> None:
    match seq:
        case value1, value2:
            return value1, value2
        case _:
            raise Exception('Incorrect sequence!')