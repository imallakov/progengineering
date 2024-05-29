def simple_map(transformation, nums):
    return list(map(transformation, nums))


# Пример использования функции
values = [1, 3, 1, 5, 7]
operation = lambda x: x + 5
print(*simple_map(operation, values))  # Вывод: 6 8 6 10 12
