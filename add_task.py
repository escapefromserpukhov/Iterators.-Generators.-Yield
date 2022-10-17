
class FlatIteratorEnhanced:

    def __init__(self, multi_list):
        """Определяет атрибут для хранения списка списков"""
        self.multi_list = multi_list

    def __iter__(self):
        """Определяет атрибуты для итерации по списку"""
        self.iterators_queue = []  # определяем вложенный список для добавления элементов очереди итераторов
        self.current_iterator = iter(self.multi_list)  # определяем итератор для списка
        return self

    def __next__(self):
        """Определяет и возвращает следущий элемент списка списков"""
        while True:
            try:
                self.current_element = next(self.current_iterator)   # получаем следующий элемент списка
            except StopIteration:  # или получаем исключение, ели следующего элемента нет
                if not self.iterators_queue:  # если не осталось элементов в очереди, возвращаем исключение
                    raise StopIteration
                else:
                    self.current_iterator = self.iterators_queue.pop()  # или получаем следующий элемент очереди
                    continue
            if isinstance(self.current_element, list):  # проверяем тип следующего элемента (список или нет)
                self.iterators_queue.append(self.current_iterator)  # если список, то добавляем в очередь
                self.current_iterator = iter(self.current_element)  # и смещаем указатель текущего итератора
            else:  # если элемент не список, то возвращаем этот элемент
                return self.current_element


def flat_generator_enhanced(multi_list):
    """Генератор позволяет  возвращать эелементы из списка списков с любым уровнем вложености"""
    for elem in multi_list:
        if isinstance(elem, list):  # проверяем тип следующего элемента (список или нет)
            for sub_elem in flat_generator_enhanced(elem):  # если список, то снова рекурсивно вызываем этот же генратор
                yield sub_elem
        else:
            yield elem  # если элемент не список, то возвращаем этот элемент


if __name__ == '__main__':

    nested_list = [
        ['a', ['b'], 'c'],
        ['d', 'e', [[[[['f']]]]], 'h', False],
        [1, [[[2]]], None],
    ]

    print('*' * 20)
    print('Вызов расширенного итератора')
    for item in FlatIteratorEnhanced(nested_list):
        print(item)
    print('*' * 20)

    print('_' * 20)
    print('Вызов расширенного генераторра')
    for item in flat_generator_enhanced(nested_list):
        print(item)
    print('_' * 20)

    print('+' * 20)
    print('Вызов компрехеншен')
    flat_list = [item for item in FlatIteratorEnhanced(nested_list)]
    print(flat_list)
    print('+' * 20)
