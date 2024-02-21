# Необходимо найти наибольшее количество идущих подряд символов кириллицы.
def max_cyrillic_order(input_string):
    max_count = 0
    current_count = 0

    for char in input_string:
        if 'а' <= char <= 'я' or 'А' <= char <= 'Я':  # символ находится в диапазоне кириллических букв
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count




print("Выберите задачу:")
print("1. Найти наибольшее количество идущих подряд символов кириллицы")
print("2. Найти минимальное натуральное число в строке")
print("3. Найти максимальное количество идущих подряд цифр в строке")

choice = input("Введите номер задачи: ")

if choice == '1':
    input_string = input("Введите строку: ")
    result = max_cyrillic_order(input_string)
    print("Наибольшее количество идущих подряд символов кириллицы:", result)
else:
    print("Некорректный выбор задачи.")
