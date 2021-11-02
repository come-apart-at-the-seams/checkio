def backward_string(val: str) -> str:
    # your code here
    str_copy = ''
    ln = len(val)
    i = 0
    while i < ln:
        str_copy = val[i] + str_copy[:]
        i += 1

    return str_copy


if __name__ == '__main__':
    print("Example:")

    print(backward_string('val'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
    print("Coding complete? Click 'Check' to earn cool rewards!")
