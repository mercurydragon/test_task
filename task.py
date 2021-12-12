from typing import List, Set


# В первом задании не указано, нужно ли выводить повторяющиеся элементы, поэтому, вот 2 варианта - с сохранением
# элементов и без него

def list_subtract_save_doubles(first: List, second: List) -> List:
    """
    :param first: First list
    :param second: List that will be subtracted from first.
    :return: Elements from the first list that does not contain in the second, save double value if it exists.
    Time complexity is O(n^2).
    """
    return [item for item in first if item not in second]


def list_subtract_unique(first: List, second: List) -> Set:
    """
    :param first: First list
    :param second: List that will be subtracted from firts.
    :return: Elements from the first list that does not contain in the second, without doubles.
    Time complexity is O(n).
    """
    return set(first) - set(second)


def remove_zeros(array: List[int]) -> List[int]:
    """
    :param array: List for removing zeros
    :return: List without zeros
    Time complexity is O(n).
    Space complexity is O(1).
    """
    i = 0
    max_i = len(array)
    while i < max_i:
        if array[i] == 0:
            del array[i]
            i = i - 1
            max_i = max_i - 1
        i = i + 1
    return array


if __name__ == '__main__':
    first = [0, 1, 0, 2, 3, 0, 0, 4, 6, 0]
    second = [2, 6]
    print(list_subtract_save_doubles(first, second))  # output [0, 1, 0, 3, 0, 0, 4, 0]
    print(list_subtract_unique(first, second))  # output {0, 1, 3, 4}
    print(remove_zeros(first))   # output [1, 2, 3, 4, 6]
