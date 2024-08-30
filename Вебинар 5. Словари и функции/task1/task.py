def letter_stat(our_str):
    """Буквенная статистика
    :param our_str: строка
    :return: словарь со статистикой по буквам
    """
    letters_dict = {}  # Создаем пустой словарь для хранения статистики

    for letter in our_str:  # Проходим по каждой букве в строке
        if letter in letters_dict:  # Если буква уже есть в словаре
            letters_dict[letter] += 1  # Увеличиваем счетчик на 1
        else:
            letters_dict[letter] = 1  # Иначе, добавляем букву в словарь со значением 1

    return letters_dict  # Возвращаем словарь с количеством вхождений каждой буквы

# Пример использования
print(letter_stat('letter'))  # Вывод: {'l': 1, 'e': 2, 't': 2, 'r': 1}
