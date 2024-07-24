import re

def minimum_length_slice(first_string, second_string):
    """Срез минимальной длины
    :param first_string: первая строка
    :param second_string: вторая строка
    :return: min_slice срез минимальной длины строки second_string
    """
    pattern = f'(?=.*{first_string[0]})(?=.*{first_string[1]})(?=.*{first_string[2]})'
    matches = re.finditer(pattern, second_string)

    min_slice = min((second_string[start:end]
                     for start in range(len(second_string))
                     for end in range(start + 1, len(second_string) + 1)
                     if all(c in second_string[start:end] for c in first_string)),
                    key=len, default="")

    return min_slice


# Пример использования
first_string = 'wtf'
second_string = 'brick quz jmpy veldt whangs fox'
result = minimum_length_slice(first_string, second_string)
print(result)