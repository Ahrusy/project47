def is_palindrome(s: str) -> bool:
    # 1. Преобразуем строку к нижнему регистру
    s = s.lower()

    # 2. Удалим из строки все символы, кроме букв и цифр (игнорируем пробелы, знаки препинания и т.п.)
    s = ''.join(char for char in s if char.isalnum())

    # 3. Сравним строку с её зеркальной копией (reversed)
    return s == s[::-1]


# Пример использования функции:

# Строка: читается одинаково слева направо и справа налево
example1 = "А роза упала на лапу Азора"
result1 = is_palindrome(example1)
print(f"'{example1}' — палиндром? {result1}")  # True

# Строка: не является палиндромом
example2 = "Просто строка"
result2 = is_palindrome(example2)
print(f"'{example2}' — палиндром? {result2}")  # False
