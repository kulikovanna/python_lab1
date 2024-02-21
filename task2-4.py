import random

# Функция для перемешивания всех символов в строке
def shuffle_string(input_string):
    # Преобразуем строку в список символов
    chars = list(input_string)
    # Перемешиваем символы
    random.shuffle(chars)
    # Соединяем символы обратно в строку и возвращаем результат
    return ''.join(chars)

input_string = input("Введите строку: ")
shuffled_string = shuffle_string(input_string)
print("Перемешанная строка:", shuffled_string)

# Функция для проверки, образуют ли прописные символы строки палиндром
def is_uppercase_palindrome(input_string):
    # Преобразуем входную строку в верхний регистр
    input_string_upper = input_string.upper()
    # Проверяем, является ли строка палиндромом
    return input_string_upper == input_string_upper[::-1]

input_string = input("Введите строку: ")
result = is_uppercase_palindrome(input_string)
if result:
    print("Прописные символы строки образуют палиндром.")
else:
    print("Прописные символы строки не образуют палиндром.")
