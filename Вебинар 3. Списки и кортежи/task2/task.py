def get_list_info(lst):
    """Получение информации о списке
    :param lst: список из чисел
    :return: min_elem, max_elem, sum_list, average
    """
    min_elem = min(lst)
    max_elem = max(lst)
    sum_list = sum(lst)
    average = round(sum_list / len(lst), 2)

    return (min_elem, max_elem, sum_list, average)


# Пример использования
result = get_list_info([1, 2, 3, 4, 5, 6, 7])
print(result)  # (1, 7, 28, 4.0)
