def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    inner = text.index(begin)
    outer = text.index(end)
    # your code here
    return text[int(inner + 1) : int(outer)]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')
