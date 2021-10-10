from collections import Counter, defaultdict

def remove_all_duplicate_items(_list):
    counter = {}
    for item in _list:
        counter[item] = counter.get(item, 0) + 1
    return [item for item, count in counter.items() if count == 1]

def remove_all_duplicate_items_by_counter(_list):
    counter = Counter(_list)
    return [item for item, count in counter.items() if count == 1]

def remove_all_duplicate_items_with_defaultdict(_list):
    counter = defaultdict(int)
    for item in _list:
        counter[item] += 1
    return [item for item, count in counter.items() if count == 1]


if __name__ == '__main__':
    # Need to remove duplicates list items (type of items is integer)
    input_list = [7, 1, 1, 4, 3, 2, 5, 3, 1, 7]

    # correct result is [4, 2, 5]
    print(f'remove_all_duplicate_items={remove_all_duplicate_items(input_list)}')
    print(f'remove_all_duplicate_items_by_counter={remove_all_duplicate_items_by_counter(input_list)}')
    print(f'remove_all_duplicate_items_with_defaultdict={remove_all_duplicate_items_with_defaultdict(input_list)}')
