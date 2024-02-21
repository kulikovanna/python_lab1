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

