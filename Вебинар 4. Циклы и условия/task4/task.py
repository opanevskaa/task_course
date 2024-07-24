def multiplication_chain(num):
    """Цепочка умножений
    :param num: положительное число
    :return: количество перемножений
    """
    # Инициализируем счетчик итераций
    count = 0

    # Продолжаем цикл, пока число состоит из более чем одной цифры
    while num >= 10:
        product = 1
        while num > 0:
            product *= num % 10  # Извлекаем последнюю цифру и умножаем
            num //= 10  # Убираем последнюю цифру
        num = product  # Обновляем num на произведение цифр
        count += 1  # Увеличиваем счетчик итераций

    return count


# Примеры вызова функции
print(multiplication_chain(39))  # 3
print(multiplication_chain(999))  # 4
print(multiplication_chain(4))  # 0
print(multiplication_chain(123))  # 1
