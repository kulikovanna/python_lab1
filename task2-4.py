import random

# Функция для перемешивания всех символов в строке
def shuffle_string(input_string):
    # Преобразуем строку в список символов
    chars = list(input_string)
    # Перемешиваем символы
    random.shuffle(chars)
    # Соединяем символы обратно в строку и возвращаем результат
    return ''.join(chars)

# Функция для проверки, образуют ли прописные символы строки палиндром
def is_uppercase_palindrome(input_string):
    # Преобразуем входную строку в верхний регистр
    input_string_upper = input_string.upper()
    # Проверяем, является ли строка палиндромом
    return input_string_upper == input_string_upper[::-1]


# Функция для упорядочивания слов в строке по количеству букв в каждом слове
def sort_words_by_length(input_string):
    # поделим строку на слова
    words = input_string.split()
    # отсортируем слова по длине
    sorted_words = sorted(words, key=len) # key=len указывает, что строки должны сортироваться в соответствии с их длиной.
    # объединим отстортированные слова в строку
    return ' '.join(sorted_words)


print("Выберите задачу:")
print("1. Перемешать символы в строке")
print("2. Проверить, образуют ли прописные символы строки палиндром")
print("3. Упорядочить слова в строке по количеству букв в каждом слове")

choice = input("Введите номер задачи: ")

if choice == '1':
    input_string = input("Введите строку: ")
    shuffled_string = shuffle_string(input_string)
    print("Перемешанная строка:", shuffled_string)
elif choice == '2':
    input_string = input("Введите строку: ")
    result = is_uppercase_palindrome(input_string)
    if result:
        print("Прописные символы строки образуют палиндром.")
    else:
        print("Прописные символы строки не образуют палиндром.")
elif choice == '3':
    input_string = input("Введите строку: ")
    sorted_string = sort_words_by_length(input_string)
    print("Упорядоченные слова по количеству букв в каждом слове:", sorted_string)
else:
    print("Некорректный выбор задачи.")