import sys


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


def check_password(password):
    # Проверка длины пароля
    if len(password) < 9:
        raise LengthError("Пароль должен быть длиной не менее 9 символов")

    # Проверка наличия больших и маленьких букв
    has_upper = False
    has_lower = False
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
    if not (has_upper and has_lower):
        raise LetterError("Пароль должен содержать как большие, так и маленькие буквы")

    # Проверка наличия цифр
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if not has_digit:
        raise DigitError("Пароль должен содержать хотя бы одну цифру")

    # Проверка на наличие последовательностей из 3 букв, идущих рядом на клавиатуре
    keyboard_sequences = ["qwe", "rty", "uio", "asdf", "zxcv", "йцу", "фыв", "олд", "јкл", "ячс"]
    for i in range(len(password) - 2):
        if password[i:i + 3].lower() in keyboard_sequences:
            raise SequenceError("Пароль не должен содержать последовательностей из 3 букв, идущих рядом на клавиатуре")

    # Если все проверки пройдены, пароль считается хорошим
    return "ok"


while True:
    try:
        password = input("Введите новый пароль: ")
        if password.lower() == "ctrl+break":
            print("Bye-Bye")
            sys.exit()
        result = check_password(password)
        print(result)
        break
    except PasswordError as e:
        print(e.__class__.__name__)
    except KeyboardInterrupt:
        print("Bye-Bye")
        sys.exit()
