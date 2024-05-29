import pytest
from reverse import reverse


def test_empty_string():
    assert reverse("") == ""


def test_single_character_string():
    assert reverse("a") == "a"


def test_palindrome_string():
    assert reverse("racecar") == "racecar"


def test_non_palindrome_string():
    assert reverse("hello") == "olleh"


def test_non_string_non_iterable():
    with pytest.raises(TypeError):
        reverse(123)


def test_non_string_iterable():
    with pytest.raises(TypeError):
        reverse([1, 2, 3])
