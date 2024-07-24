def even_sum(lst):
    """Получение суммы элементов списка с четными индексами
    :param lst: список из чисел
    :return: сумму элементов с четными индексами
    """
    return sum(lst[i] for i in range(0, len(lst), 2))

# Пример использования
result = even_sum([1, 2, 3, 4, 5, 6, 7])
print(result)  # 16
