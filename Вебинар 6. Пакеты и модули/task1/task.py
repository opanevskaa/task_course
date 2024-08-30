# Определяем глобальные переменные
number = 1
string = 'Hello'

def global_changes():
    """Глобальные переменные
    :return: измененные number и string
    """
    global number, string  # Указываем, что будем изменять глобальные переменные

    # Изменяем значения глобальных переменных
    number = 5
    string = 'Hello, dear friend'

    return number, string

# Пример использования
print(global_changes())  # Вывод: (5, 'Hello, dear friend')
print(number)  # Вывод: 5
print(string)  # Вывод: 'Hello, dear friend'
