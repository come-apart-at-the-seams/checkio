from typing import Iterable


def replace_first(items: list) -> Iterable:
    if not items:
        return items

    items.append(items[0])
    items.pop(0)
    return items


if __name__ == '__main__':
    print("Example:")
    replace_first([1, 2, 3, 4])

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
