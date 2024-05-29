import re


def is_correct_mobile_phone_ru(number):
    pattern = re.compile(
        r'^(?:\+7|8)?[\s\-]?(\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}|(\d{3})\s\d{3}\s\d{2}\s\d{2})$')
    match = pattern.fullmatch(number)
    return bool(match)


def main():
    number = input("Enter a mobile phone number: ")
    if is_correct_mobile_phone_ru(number):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
