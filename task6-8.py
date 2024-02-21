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

# Найти минимальное натуральное число в строке
def min_natural_number(input_string):
    numbers = []
    current_number = ""
    for char in input_string:
        if char.isdigit(): # явл. ли цифрой
            current_number += char
        elif current_number: # есть ли непустое число
            numbers.append(int(current_number))
            current_number = "" # сброс
    if numbers:
        return min(numbers)
    else:
        return None

# Найти максимальное количество идущих подряд цифр в строке
def max_digit_order(input_string):
    max_count = 0
    count = 0
    for char in input_string:
        if char.isdigit():
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
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
elif choice == '2':
    input_string = input("Введите строку: ")
    result = min_natural_number(input_string)
    if result is not None:
        print("Минимальное натуральное число в строке:", result)
elif choice == '3':
    input_string = input("Введите строку: ")
    result = max_digit_order(input_string)
    print("Максимальное количество идущих подряд цифр в строке:", result)
else:
    print("Некорректный выбор задачи.")

