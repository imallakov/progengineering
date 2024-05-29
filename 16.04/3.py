import sys


def sum_arguments():
    if len(sys.argv) != 4:  # Проверяем количество аргументов
        return 0

    try:
        num1 = float(sys.argv[1])  # Пробуем преобразовать первый аргумент в целое число
        num2 = float(sys.argv[2])  # Пробуем преобразовать второй аргумент в целое число
        operation = sys.argv[3]
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            return num1 / num2
        else:
            return 'Invalid operation'
    except (ValueError, IndexError):  # Обрабатываем ошибки преобразования и доступа к аргументам
        return 0


result = sum_arguments()
print(result)