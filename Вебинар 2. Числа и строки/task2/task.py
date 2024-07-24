def quadratic(b, c):
    """Решение квадратного уравнения
    :param b: коэффициент b
    :param c: коэффициент c
    :return: корни квадратного уравнения
    """
    # Вычисление дискриминанта
    discriminant = b ** 2 - 4 * c
    # Вычисление корней уравнения с округлением до двух знаков после запятой
    x1 = round((-b + discriminant ** 0.5) / 2, 2)
    x2 = round((-b - discriminant ** 0.5) / 2, 2)
    return x1, x2


# Пример использования функции
b = -5
c = 4
x1, x2 = quadratic(b, c)
print(f"x1: {x1}, x2: {x2}")
