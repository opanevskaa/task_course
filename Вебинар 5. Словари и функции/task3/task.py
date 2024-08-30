def everything_for_your_cat(cats_data):
    """Котики и их владельцы
    :param cats_data: информация о котах и их владельцах
    :return: информация о котах и их владельцах в виде строки
    """
    # Создаем временный словарь для хранения информации
    owners_dict = {}

    # Заполняем словарь данными о котиках
    for cat_name, cat_age, owner_first_name, owner_last_name in cats_data:
        owner_key = f"{owner_first_name} {owner_last_name}"
        owners_dict.setdefault(owner_key, []).append(f"{cat_name}, {cat_age}")

    # Формируем строку результата
    result = ""
    for owner, cats in owners_dict.items():
        result += f"{owner}: {'; '.join(cats)}\n"

    return result.strip()  # Убираем лишний перевод строки в конце


# Пример использования
cat_data_sample = [
    ('Мартин', 5, 'Алексей', 'Егоров'),
    ('Фродо', 3, 'Анна', 'Самохина'),
    ('Вася', 4, 'Алексей', 'Егоров')
]

print(everything_for_your_cat(cat_data_sample))
# Ожидаемый вывод:
# Алексей Егоров: Мартин, 5; Вася, 4
# Анна Самохина: Фродо, 3
