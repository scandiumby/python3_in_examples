def get_count_each_chars_in_string(input_string: str) -> dict:
    result = dict.fromkeys(set(input_string), 0)
    for char in input_string:
        result[char] += 1
    return result

def get_count_unique_chars_in_string(input_string: str) -> int:
    return len(set(input_string))


def get_russian_chars_not_included_in_string(input_string: str) -> set:
    russian_alphabet = {chr(char_code) for char_code in range(0x410, 0x450)}
    russian_alphabet.update(('Ё', 'ё'))
    return russian_alphabet.difference(set(input_string))


if __name__ == '__main__':
    test_string = 'аааБББрСя'
    print(f'{test_string=}')
    print(f'{get_count_each_chars_in_string(test_string)=}')
    print(f'{get_count_unique_chars_in_string(test_string)=}')