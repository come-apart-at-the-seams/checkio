def end_zeros(num: int) -> int:
    # your code here
    if num == 0:
        return 1
    zero_check = 0
    is_zero = True
    while is_zero:
        if num % 10 == 0:
            num //= 10
            zero_check += 1
        else:
            is_zero = False
    return zero_check


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
