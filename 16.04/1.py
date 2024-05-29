import sys


def sum_arguments():
    if len(sys.argv) != 3:  # Проверяем количество аргументов
        return 0

    try:
        num1 = int(sys.argv[1])  # Пробуем преобразовать первый аргумент в целое число
        num2 = int(sys.argv[2])  # Пробуем преобразовать второй аргумент в целое число
        return num1 + num2
    except (ValueError, IndexError):  # Обрабатываем ошибки преобразования и доступа к аргументам
        return 0


result = sum_arguments()
print(result)
