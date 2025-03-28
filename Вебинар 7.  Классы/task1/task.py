class Segment:
    def __init__(self, first_point, second_point):
        self.first_point = first_point
        self.second_point = second_point

    def length(self):
        """Вычисление длины отрезка"""
        x1, y1 = self.first_point
        x2, y2 = self.second_point
        return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)

    def x_axis_intersection(self):
        """Пересечение оси абсцисс"""
        y1 = self.first_point[1]
        y2 = self.second_point[1]
        return y1 * y2 <= 0

    def y_axis_intersection(self):
        """Пересечение оси ординат"""
        x1 = self.first_point[0]
        x2 = self.second_point[0]
        return x1 * x2 <= 0
