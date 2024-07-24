def delete_symbols(string):
    """Удаление символов с нечетными индексами
    :param string: строка
    :return: строку без символов с нечетными индексами исходной строки
    """
    new_string = string[::2]  # Срез с шагом 2, начиная с 0
    return new_string

# Пример использования
string = 'Hello World'
result = delete_symbols(string)
print(result)