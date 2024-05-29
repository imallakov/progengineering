def is_palindrome(data):
    return data == data[::-1]


def test_is_palindrome():
    assert is_palindrome("level") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("madam") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("python") == False
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    print("YES" if all(test(is_palindrome) for test in tests) else "NO")


tests = [
    lambda f: f("level"),
    lambda f: f("hello"),
    lambda f: f("madam"),
    lambda f: f("racecar"),
    lambda f: f("python"),
    lambda f: f(""),
    lambda f: f("a")
]

test_is_palindrome()
