import pytest


def count_chars(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def test_count_chars_with_string():
    assert count_chars("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    assert count_chars("Python") == {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}
    assert count_chars("") == {}


def test_count_chars_with_non_string():
    with pytest.raises(TypeError):
        count_chars(123)
    with pytest.raises(TypeError):
        count_chars([1, 2, 3])
    with pytest.raises(TypeError):
        count_chars(None)
