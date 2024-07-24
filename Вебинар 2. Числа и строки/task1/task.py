def square_calculation(a):
    """Вычисление квадрата
    :param a: сторона квадрата
    :return: периметр квадрата, площадь квадрата и диагональ квадрата
    """

    # Вычисление периметра квадрата
    perimeter = 4 * a
    # Вычисление площади квадрата с округлением до двух знаков после запятой
    square = round(a * a, 2)
    # Вычисляем диагональ квадрата с округлением до двух знаков после запятой
    diagonal = round(a * (2 ** 0.5), 2)
    return perimeter, square, diagonal


# Пример использования функции
a = 10
perimeter, square, diagonal = square_calculation(a)
print(f'Perimeter: {perimeter}, Square: {square}, Diagonal: {diagonal}')
