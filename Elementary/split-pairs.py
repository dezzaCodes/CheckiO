def split_pairs(a):
    # your code here
    if (len(a) % 2) == 1:
        a = a + '_'
    print(a)
    ans = []
    i = 0
    while i < len(a):
        ans.append(a[i:i + 2])
        i = i + 2
    return ans


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
