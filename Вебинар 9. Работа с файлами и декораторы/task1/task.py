# todo Здесь нужно написать код

import os

# Убедимся, что папка "test_file" существует
os.makedirs("test_file", exist_ok=True)

# Пути к файлам
input_file = "test_file/task1_data.txt"
output_file = "test_file/task1_answer.txt"

# Читаем файл, удаляем цифры и записываем результат
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# Убираем цифры из текста
clean_text = "".join(char for char in text if not char.isdigit())

# Записываем результат в новый файл
with open(output_file, "w", encoding="utf-8") as f:
    f.write(clean_text)
