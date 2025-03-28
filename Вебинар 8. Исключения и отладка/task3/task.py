def segment(first_point, second_point):
    """Сумма всех координат точек или текст исключения наоборот.
    :param first_point: координаты первой точки (tuple)
    :param second_point: координаты второй точки (tuple)
    :return: сумма всех координат или перевернутый текст исключения
    """
    try:
        result = sum(first_point) + sum(second_point)
    except Exception as e:
        return str(e)[::-1]  # Переворачиваем текст исключения
    else:
        return result
