import os


def test_file_path(file_path):
    """Путь до файла
    :param file_path: абсолютный путь до файла
    :return: название файла без расширения, название диска и корневая папка
    """
    # Получаем название файла без расширения
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    # Получаем название диска
    disk_name = file_path[0]  # Первый символ - это диск, например, 'C'

    # Получаем корневую папку (один уровень выше)
    root_folder = os.path.basename(os.path.dirname(file_path))

    return file_name, disk_name, root_folder


# Пример использования функции
file_path = r'C:\Python312\python.exe'
file_name, disk_name, root_folder = test_file_path(file_path)
print(f"File Name: {file_name}, Disk Name: {disk_name}, Root Folder: {root_folder}")
