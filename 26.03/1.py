def check_password(password):
    # Проверка длины пароля
    if len(password) < 8:
        return "error"

    # Проверка наличия больших и маленьких букв
    has_upper = False
    has_lower = False
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
    if not (has_upper and has_lower):
        return "error"

    # Проверка наличия цифр
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if not has_digit:
        return "error"

    # Проверка на наличие последовательностей из 3 букв, идущих рядом на клавиатуре
    keyboard_sequences = ["qwe", "rty", "uio", "asdf", "zxcv", "йцу", "фыв", "олд", "јкл", "ячс"]
    for i in range(len(password) - 2):
        if password[i:i + 3].lower() in keyboard_sequences:
            return "error"

    # Если все проверки пройдены, пароль считается хорошим
    return "ok"


def main():
    password = input("Enter the password: ")
    print(check_password(password))


main()
