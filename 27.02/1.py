def arithmetic_operation(operation):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }

    return operations.get(operation, None)


# Пример использования функции
operation = arithmetic_operation('+')
print(operation(1, 4))  # Вывод: 5
