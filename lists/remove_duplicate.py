
from collections import Counter


def remove_all_duplicate_items_by_counter(_list):
    counter = Counter(_list)
    return [item for item, count in counter.items() if count == 1]


if __name__ == '__main__':
    # Need to remove duplicates list items (type of items is integer)
    input_list = [7, 1, 1, 4, 3, 2, 5, 3, 1, 7]  # correct result is [4, 2, 5]
    print(remove_all_duplicate_items_by_counter(input_list))
