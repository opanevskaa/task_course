def sum_digits(num):
    """Нахождение суммы цифр числа
    :param num: число
    :return: сумма цифр числа
    """
    # Преобразуем число в строку, чтобы пройтись по каждой цифре
    num_str = str(num)

    # Инициализируем сумму цифр
    total_sum = 0

    # Проходим по каждой цифре в строковом представлении числа
    for digit in num_str:
        # Преобразуем цифру обратно в целое число и добавляем к сумме
        total_sum += int(digit)

    return total_sum


# Примеры вызова функции
print(sum_digits(39))  # 12
print(sum_digits(999))  # 27
print(sum_digits(4))  # 4
print(sum_digits(12345))  # 15
