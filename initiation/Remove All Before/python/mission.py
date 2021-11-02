from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    # your code here
    del_num = -1
    flag = 0
    for i in items:
        flag += 1
        if i == border:
            del_num = flag
            break
    if del_num == -1:
        return items
    return items[del_num - 1:]


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))
    print(list(remove_all_before([1, 1, 2, 2, 3, 3], 2)))
    print(list(remove_all_before([1, 1, 5, 6, 7], 2)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")
