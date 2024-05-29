def is_correct_mobile_phone_number_ru(number):
    # Удаляем все пробелы и дефисы из номера
    number = number.replace(" ", "").replace("-", "")

    # Проверяем, что номер начинается с 8 или +7
    if not number.startswith("8") and not number.startswith("+7"):
        return False

    # Проверяем, что после 8 или +7 идет 3-значный код оператора
    if len(number) < 11 or not number[1:4].isdigit():
        return False

    # Проверяем, что после кода оператора идет 7 цифр
    if not number[4:].isdigit() or len(number[4:]) != 7:
        return False

    return True


def test_is_correct_mobile_phone_number_ru():
    # Тестовые данные
    valid_numbers = [
        "+7 999 123-45-67",
        "+7(900)1234567",
        "89001234567",
        "+7(999) 123 45 67"
    ]
    invalid_numbers = [
        "7 999 123-45-67",
        "+7(900)123456",
        "8900123456789",
        "+7(9aa)1234567",
        "+7 999 12-3-45-67"
    ]

    # Выполнение тестов
    for number in valid_numbers:
        if not is_correct_mobile_phone_number_ru(number):
            print(f"{number} - NO")
        else:
            print(f"{number} - YES")

    for number in invalid_numbers:
        if is_correct_mobile_phone_number_ru(number):
            print(f"{number} - NO")
        else:
            print(f"{number} - YES")


# Запуск тестирующей программы
test_is_correct_mobile_phone_number_ru()
