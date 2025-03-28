class RomanNums:
    roman_to_arabic = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }

    def __init__(self, roman):
        self.roman = roman

    def from_roman(self):
        """Переводит римское число в арабское."""
        arabic = 0
        prev_value = 0

        for char in reversed(self.roman):
            value = self.roman_to_arabic[char]
            if value < prev_value:
                arabic -= value
            else:
                arabic += value
            prev_value = value

        return arabic

    def is_palindrome(self):
        """Проверяет, является ли арабское число палиндромом."""
        arabic = self.from_roman()
        arabic_str = str(arabic)
        return arabic_str == arabic_str[::-1]


# Пример использования:
roman_number = RomanNums('MMMCCLXIII')
print(roman_number.from_roman())  # 3263

roman_palindrome = RomanNums('CMXCIX')
print(roman_palindrome.is_palindrome())  # True