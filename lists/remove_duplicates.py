# Need to remove duplicates list items (type of items is integer)
from collections import Counter


def remove_list_duplicates(_list):
    counter = Counter(_list)
    return [item for item in counter if counter[item] == 1]

if __name__ == '__main__':
    input_list = [1,4,3,2,5,3,1]
    print(remove_list_duplicates(input_list))