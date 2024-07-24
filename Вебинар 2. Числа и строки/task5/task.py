def sum_and_multiplication(a, b):
    """Сумма и произведение двух чисел
    :param a: первое число
    :param b: второе число
    :return: сумму и произведение
    """

    a_b_sum = f"{a} + {b} = {a + b}"
    a_b_multi = f"{a} * {b} = {a * b}"
    return a_b_sum, a_b_multi


# Пример использования
a, b = 5, 10
result_sum, result_multi = sum_and_multiplication(a, b)
print(result_sum)  # '5 + 10 = 15'
print(result_multi)  # '5 * 10 = 50'