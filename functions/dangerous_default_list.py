from typing import Dict, Union


# Python 3.8 tested
def bad_function(value: int, seq: list = []) -> Dict[str, Union[int, list]]:
    seq.append(value)
    return {"id(seq)": id(seq), "seq": seq}


# Python 3.8 tested
def good_function(value: int, seq: list = None) -> Dict[str, Union[int, list]]:
    if seq is None:
        seq = []
    seq.append(value)
    return {"id(seq)": id(seq), "seq": seq}


if __name__ == '__main__':
    for i in range(3):
        print(f'{bad_function(i)=}')
        print(f'{good_function(i)=}')
