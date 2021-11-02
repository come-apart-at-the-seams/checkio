def number_length(a: int) -> int:
    # your code her
    q = 0
    if a == 0:
        return 1
    while a != 0:
        a //= 10
        q += 1
    return q


if __name__ == '__main__':
    print("Example:")
    print(number_length(10))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert number_length(10) == 2
    assert number_length(0) == 1
    assert number_length(4) == 1
    assert number_length(44) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
