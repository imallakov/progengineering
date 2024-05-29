def strip_punctuation_ru(data):
    import string
    translator = str.maketrans('', '', string.punctuation)
    return ' '.join(word.translate(translator) for word in data.split())


def test_strip_punctuation_ru():
    assert strip_punctuation_ru("А роза упала на лапу Азора!") == "А роза упала на лапу Азора"
    assert strip_punctuation_ru("Привет, мир!") == "Привет мир"
    assert strip_punctuation_ru("Скажи, что-нибудь!") == "Скажи что нибудь"
    assert strip_punctuation_ru("Это --- тест!") == "Это тест"
    assert strip_punctuation_ru("123456") == "123456"
    assert strip_punctuation_ru("!@#$%^&*()_+-={}[]|\\:;\"'<>,./?") == ""
    print("YES" if all(test(strip_punctuation_ru) for test in tests) else "NO")


tests = [
    lambda f: f("А роза упала на лапу Азора!"),
    lambda f: f("Привет, мир!"),
    lambda f: f("Скажи, что-нибудь!"),
    lambda f: f("Это --- тест!"),
    lambda f: f("123456"),
    lambda f: f("!@#$%^&*()_+-={}[]|\\:;\"'<>,./?")
]
