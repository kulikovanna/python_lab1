# Вариант 11

# Функция 1: Найти количество делителей числа, не делящихся на 3
def count_non_divisible_by_three_divisors(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0 and i % 3 != 0:
            count += 1
    return count

number = int(input("Введите число: "))
result = count_non_divisible_by_three_divisors(number)
print("Количество делителей, не делящихся на 3: ", result)

# Функция 2: Найти минимальную нечетную цифру числа
def find_min_odd_digit(number):
    min_odd_digit = float('inf')
    while number > 0:
        digit = number % 10
        if digit % 2 != 0 and digit < min_odd_digit:
            min_odd_digit = digit
        number //= 10
    return min_odd_digit if min_odd_digit != float('inf') else None

number = int(input("Введите число: "))
result = find_min_odd_digit(number)
print("Минимальная нечетная цифра: ", result)

# Функция 3: Найти сумму всех делителей числа, взаимно простых с
# суммой цифр числа и не взаимно простых с произведением цифр числа
from math import gcd
def sum_of_divisors_with_conditions(number):
    # Считаем сумму
    digit_sum = sum(int(digit) for digit in str(number))

    # Считаем произведение
    digit_product = 1
    for digit in str(number):
        digit_product *= int(digit)

    # сумма делителей
    divisor_sum = 0

    for i in range(1, number + 1):
        # проверяем, является ли текущее число делителем number
        if number % i == 0:
            # Проверяем условия взаимной простоты и добавляем число к сумме делителей, если условия выполняются
            if gcd(i, digit_sum) == 1 and gcd(i, digit_product) != 1:
                divisor_sum += i

    return divisor_sum

number = int(input("Введите число: "))
result = sum_of_divisors_with_conditions(number)
print("Сумма всех делителей числа в указанных условиях равна: ", result)