def move_zeros(lst):
    """Перемещение нулей
    :param lst: список из цифр
    :return: список из цифр с нулями в конце
    """
    # Сначала создаем список всех ненулевых элементов
    non_zero_elements = [num for num in lst if num != 0]

    # Затем добавляем нужное количество нулей в конец списка
    zeros_count = len(lst) - len(non_zero_elements)
    result = non_zero_elements + [0] * zeros_count

    return result


# Примеры вызова функции
print(move_zeros([1, 0, 1, 2, 0, 1, 3]))  # [1, 1, 2, 1, 3, 0, 0]
print(move_zeros([0, 0, 1, 2, 3]))  # [1, 2, 3, 0, 0]
print(move_zeros([4, 5, 6, 0, 0, 0]))  # [4, 5, 6, 0, 0, 0]
print(move_zeros([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
