def memorize(function):
    cache = {}  # Словарь для хранения результатов

    def wrapper(weight, speed):
        key = (weight, speed)  # Ключ - кортеж аргументов
        if key not in cache:
            cache[key] = function(weight, speed)  # Вычисляем и сохраняем
        return cache[key], cache  # Возвращаем результат и словарь

    return wrapper


# Не изменяем код функции
@memorize
def get_kinetic_energy(weight, speed):
    """Кинетическая энергия
    :param weight: масса
    :param speed: скорость
    :return: кинетическую энергию
    """
    return (weight * speed ** 2) / 2