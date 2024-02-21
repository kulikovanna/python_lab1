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