def josephus_task(num_people, kill_num):
    """Задача Иосифа Флавия
    :param num_people: количество воинов
    :param kill_num: номер воина
    :return: номер последнего оставшегося воина
    """
    # Инициализируем список воинов
    people = list(range(1, num_people + 1))

    # Индекс текущего воина, с которого начинаем отсчет
    index = 0

    # Пока в списке больше одного воина
    while len(people) > 1:
        # Находим индекс воина, который будет выведен из круга
        index = (index + kill_num - 1) % len(people)
        # Удаляем этого воина из списка
        people.pop(index)

    # Возвращаем последнего оставшегося воина
    return people[0]


# Примеры вызова функции
print(josephus_task(7, 3))  # 4
print(josephus_task(5, 2))  # 3
print(josephus_task(10, 1))  # 10
print(josephus_task(1, 3))  # 1