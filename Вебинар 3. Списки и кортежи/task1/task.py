def modification(lst):
    """Изменение списка
    :param lst: список
    :return: преобразованный список
    """
    lst[0], lst[-1] = lst[-1], lst[0]  # Меняем местами первый и последний элементы
    return lst

# Пример использования
result = modification([1, 2, 3])
print(result)  # [3, 2, 1]
