class PublicTransport:
    def __init__(self, brand, engine_power, year, color, max_speed):
        self.brand = brand
        self._engine_power = engine_power  # защищённый атрибут
        self.year = year
        self.color = color
        self.max_speed = max_speed

    @property
    def info(self):
        """Возвращает информацию о транспорте."""
        return f"Марка: {self.brand}, Цвет: {self.color}, Год: {self.year}, Мощность: {self._engine_power} л.с."


class Bus(PublicTransport):
    def __init__(self, brand, engine_power, year, color, max_speed, passengers, park, fare):
        super().__init__(brand, engine_power, year, color, max_speed)
        self.passengers = passengers
        self.__park = None  # приватный атрибут
        self.park = park  # Используем setter
        self._fare = fare  # защищённый атрибут

    @property
    def park(self):
        """Возвращает номер парка."""
        return self.__park

    @park.setter
    def park(self, value):
        """Проверяет, что номер парка в диапазоне 1000-9999."""
        assert 1000 <= value <= 9999, "Номер парка должен быть в диапазоне 1000-9999"
        self.__park = value


class Tram(PublicTransport):
    def __init__(self, brand, engine_power, year, color, max_speed, route, path, fare):
        super().__init__(brand, engine_power, year, color, max_speed)
        self.__route = route  # приватный атрибут
        self.path = path
        self._fare = fare  # защищённый атрибут

    @property
    def how_long(self):
        """Вычисляет время прохождения маршрута."""
        return self.max_speed / (4 * self.path) if self.path > 0 else float('inf')


# Пример использования:
bus = Bus("Mercedes", 200, 2020, "синий", 120, 50, 1234, 50)
print(bus.info)  # Информация о транспорте
print(bus.park)  # 1234

tram = Tram("Siemens", 150, 2019, "красный", 80, "Маршрут 5", 20, 30)
print(tram.how_long)  # Время прохождения маршрута
