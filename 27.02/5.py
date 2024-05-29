def same_by(characteristic, objects):
    return all(characteristic(obj) == characteristic(objects[0]) for obj in objects)


# Пример использования
values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
