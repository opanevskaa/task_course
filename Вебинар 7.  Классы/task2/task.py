from collections import Counter

class PersonInfo:
    def __init__(self, full_name, age, *departments):
        self.full_name = full_name
        self.age = age
        self.departments = departments

    def short_name(self):
        """Возвращает строку в формате Фамилия И."""
        name, surname = self.full_name.split()
        return f"{surname} {name[0]}."

    def path_deps(self):
        """Возвращает путь подразделений, соединённых ' --> '"""
        return " --> ".join(self.departments)

    def new_salary(self):
        """Вычисляет новую зарплату по формуле"""
        text = "".join(self.departments)  # Объединяем все подразделения в одну строку
        letter_counts = Counter(text)  # Подсчитываем вхождения букв
        most_common_counts = [count for _, count in letter_counts.most_common(3)]  # Берём 3 самых частых
        total_count = sum(most_common_counts)  # Суммируем их вхождения
        return 1337 * self.age * total_count  # Вычисляем зарплату

# Пример использования
person = PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты')

print(person.short_name())  # 'Шленский А.'
print(person.path_deps())   # 'Разработка --> УК --> Автотесты'
print(person.new_salary())  # 385056