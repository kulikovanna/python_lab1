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

