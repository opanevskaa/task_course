def flatten_and_sort(array):
    """Преобразование двумерного массива в плоский список
    :param array: двумерный массив
    :return: плоский список
    """
    # Сначала создаем пустой список для хранения всех чисел
    flat_list = []

    # Проходим по всем подспискам и добавляем их элементы в flat_list
    for sublist in array:
        flat_list.extend(sublist)

    # Сортируем полученный плоский список
    flat_list.sort()

    return flat_list


# Примеры вызова функции
print(flatten_and_sort([[3, 2, 1], [4, 6], [], [5]]))  # [1, 2, 3, 4, 5, 6]
print(flatten_and_sort([[10, 9, 8], [7, 5], [6], [4, 3, 2, 1]]))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(flatten_and_sort([[], [], []]))  # []
print(flatten_and_sort([[5, 3, 9], [0, -1], [7], [2, 2, 8]]))  # [-1, 0, 2, 2, 3, 5, 7, 8, 9]