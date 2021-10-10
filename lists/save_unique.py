from collections import defaultdict


def save_only_unique_items_by_defaultdict(_list):
    counter = defaultdict(int)
    result = []
    for item in _list:
        counter[item] += 1
        if counter[item] == 1:
            result.append(item)
    return result

if __name__ == "__main__":
    # Need to save only one item for all values in list
    input_list = [7, 1, 1, 4, 3, 2, 5, 3, 1, 7]  # correct result is [7, 1, 4, 3, 2, 5]
    print(save_only_unique_items_by_defaultdict(input_list))