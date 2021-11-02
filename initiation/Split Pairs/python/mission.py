def split_pairs(a):
    if len(a)%2 == 1:
        a = a + '_'

    array = []
    for i in range(len(a)):
        if i%2 == 1:
            tmp = str(a[i-1]) + str(a[i])
            array.append(tmp)

    return array


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
