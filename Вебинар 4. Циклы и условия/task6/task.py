def create_phone_number(num_tuple):
    """Создание номера телефона
    :param num_tuple: кортеж из цифр
    :return: строку в виде номера телефона
    """
    # Форматируем строку в виде номера телефона
    phone_number = "({}{}{}) {}{}{}-{}{}{}{}".format(*num_tuple)
    return phone_number

# Примеры вызова функции
print(create_phone_number((1, 2, 3, 4, 5, 6, 7, 8, 9, 0)))  # "(123) 456-7890"
print(create_phone_number((9, 8, 7, 6, 5, 4, 3, 2, 1, 0)))  # "(987) 654-3210"
print(create_phone_number((0, 0, 0, 1, 2, 3, 4, 5, 6, 7)))  # "(000) 123-4567"
