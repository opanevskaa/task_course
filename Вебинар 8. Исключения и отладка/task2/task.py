class Trigon:
    def __init__(self, *args):
        """Инициализация треугольника с проверкой входных данных."""
        # Проверяем количество аргументов
        if len(args) != 3:
            raise IndexError(f'Передано {len(args)} аргументов, а ожидается 3')

        # Проверяем, что все стороны - числа
        if not all(isinstance(side, (int, float)) for side in args):
            raise TypeError('Стороны должны быть числами')

        # Проверяем, что все стороны положительные
        if any(side <= 0 for side in args):
            raise ValueError('Стороны должны быть положительными')

        # Проверяем неравенство треугольника
        a, b, c = args
        if not (a + b > c and a + c > b and b + c > a):
            raise Exception('Не треугольник')

        # Если все проверки пройдены, сохраняем стороны
        self.sides = args
