def string_concatenation(str1, str2):
    """Объединение строк
    :param str1: первая строка
    :param str2: вторая строка
    :return: преобразованную строку
    """

    # Меняем местами первые два символа строк
    if len(str1) < 2 or len(str2) < 2:
        return str1 + ' ' + str2  # если одна из строк слишком короткая

    new_str1 = str2[:2] + str1[2:]  # Первые два символа str2 + остаток str1
    new_str2 = str1[:2] + str2[2:]  # Первые два символа str1 + остаток str2

    # Объединяем строки с пробелом
    result_string = new_str1 + ' ' + new_str2

    return result_string


# Пример использования функции
str1 = "Апельсин"
str2 = "Груша"
result_string = string_concatenation(str1, str2)
print(result_string)  # Вывод: "Грельсин Апуша"