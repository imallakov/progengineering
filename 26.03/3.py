def check_password(password):
    try:
        # Проверка длины пароля
        assert len(password) >= 9, "Пароль должен быть длиной не менее 9 символов"

        # Проверка наличия больших и маленьких букв
        has_upper = False
        has_lower = False
        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
        assert has_upper and has_lower, "Пароль должен содержать как большие, так и маленькие буквы"

        # Проверка наличия цифр
        has_digit = False
        for char in password:
            if char.isdigit():
                has_digit = True
                break
        assert has_digit, "Пароль должен содержать хотя бы одну цифру"

        # Проверка на наличие последовательностей из 3 букв, идущих рядом на клавиатуре
        keyboard_sequences = ["qwe", "rty", "uio", "asdf", "zxcv", "йцу", "фыв", "олд", "јкл", "ячс"]
        for i in range(len(password) - 2):
            assert password[
                   i:i + 3].lower() not in keyboard_sequences, "Пароль не должен содержать последовательностей из 3 букв, идущих рядом на клавиатуре"

        # Если все проверки пройдены, пароль считается хорошим
        return "ok"

    except AssertionError as e:
        return f"error: {e}"
    except Exception as e:
        return f"error: {e}"


print(check_password("MyPassword123"))  # Выведет "ok"
print(check_password("short"))  # Выведет "error: Пароль должен быть длиной не менее 9 символов"
print(check_password(123456))  # Выведет "error: 'int' object is not iterable"
