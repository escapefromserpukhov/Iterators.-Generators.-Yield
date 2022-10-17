class FlatIterator:

    def __init__(self, multi_list):
        """Определяет атрибут для хранения списка списков"""
        self.multi_list = multi_list

    def __iter__(self):
        """Определяет атрибуты для итерации по списку"""
        self.list_iter = iter(self.multi_list)  # определяем итератор для списка
        self.nested_list = []  # определяем вложенный список для добавления элементов
        self.cursor = -1  # смещаем курсор за границу списка
        return self

    def __next__(self):
        """Определяет и возвращает следущий элемент списка списков"""
        self.cursor += 1
        if len(self.nested_list) == self.cursor:  # если курсор в конце вложенного списка, то "обнуляем" список и курсор
            self.nested_list = None
            self.cursor = 0
            while not self.nested_list:  # если вложенные списки закончились, то получаем stop iteration
                self.nested_list = next(self.list_iter)  # если  список пустой, то получаем следующий вложенный список
        return self.nested_list[self.cursor]


def flat_generator(my_list):
    """Генератор позволяет  возвращать эелементы из списка списков с двойным уровнем вложености"""
    for sub_list in my_list:
        for elem in sub_list:
            yield elem


if __name__ == '__main__':

    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    print('*' * 20)
    print('Вызов итератора')
    for item in FlatIterator(nested_list):
        print(item)
    print('*' * 20)

    print('_' * 20)
    print('Вызов компрехеншен')
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    print('_' * 20)

    print('+' * 20)
    print('Вызов генератора')
    for item in flat_generator(nested_list):
        print(item)
    print('+' * 20)
