def which_triangle(a, b, c):
    """Определение типа треугольника
    :param a: длина стороны
    :param b: длина стороны
    :param c: длина стороны
    :return: тип треугольника
    """
    # Проверка возможности построить треугольник
    if a + b <= c or a + c <= b or b + c <= a:
        return 'Не треугольник'

    # Проверка типа треугольника
    if a == b == c:
        return 'Равносторонний'
    elif a == b or a == c or b == c:
        return 'Равнобедренный'
    else:
        return 'Обычный'


# Примеры вызова функции
print(which_triangle(1, 1, 1))  # 'Равносторонний'
print(which_triangle(1, 2, 3))  # 'Не треугольник'
print(which_triangle(2, 2, 3))  # 'Равнобедренный'
print(which_triangle(3, 4, 5))  # 'Обычный'