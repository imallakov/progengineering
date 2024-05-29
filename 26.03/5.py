class DefaultList(list):
    def __init__(self, default_value=None):
        self.default_value = default_value

    def __getitem__(self, index):
        try:
            return super().__getitem__(index)
        except IndexError:
            return self.default_value


my_list = DefaultList(default_value=0)
print(my_list[0])  # Выведет 0
print(my_list[10])  # Выведет 0

my_list = DefaultList(default_value="N/A")
print(my_list[0])  # Выведет "N/A"
print(my_list[10])  # Выведет "N/A"
