def repeats(our_str):
    """Повторы букв
    :param our_str: строка
    :return: новая строка с повторами букв
    """
    letter_counts = letter_stat(our_str)  # Получаем словарь с количеством вхождений каждой буквы
    result_str = ""  # Инициализируем пустую строку для результата

    for letter in our_str:  # Проходим по каждой букве в исходной строке
        result_str += letter * letter_counts[letter]  # Добавляем букву в результат столько раз, сколько она встречается

    return result_str  # Возвращаем строку с повторами

# Пример использования
print(repeats('letter'))  # Вывод: 'leetteerr'

