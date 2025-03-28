def three_most_expensive_purchases():
    """Три самые дорогие покупки
    :return: сумму трех самых дорогих покупок
    """
    file_path = "test_file/task_2.txt"

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    purchases = []
    current_purchase = 0

    for line in lines:
        line = line.strip()
        if line:  # Если строка не пустая, добавляем цену к текущей покупке
            current_purchase += int(line)
        else:  # Пустая строка — конец покупки
            if current_purchase > 0:
                purchases.append(current_purchase)
            current_purchase = 0

    # Добавляем последнюю покупку, если файл не заканчивается пустой строкой
    if current_purchase > 0:
        purchases.append(current_purchase)

    # Если покупок меньше 3, сумма всех возможных
    most_expensive_purchases = sum(sorted(purchases, reverse=True)[:3])

    return most_expensive_purchases