# Отсортировать: В порядке увеличения среднего веса ASCII-кода символа строки.
def average_ascii_weight(word):
    total_weight = 0
    for char in word:
        total_weight += ord(char)
    return total_weight / len(word) if word else 0

def sort_by_average_weight(strings):
    return sorted(strings, key=average_ascii_weight)

# Отсортировать: В порядке увеличения медианного значения выборки строк (прошлое медианное значение удаляется из выборки и
# производится поиск нового медианного значения).

def median_length(strings):
    lengths = [len(s) for s in strings]
    sorted_lengths = sorted(lengths)
    n = len(sorted_lengths)
    mid = n // 2 #индекс ср элемента
    if n % 2 == 0:
        return sorted_lengths[mid] # если количество элементов четное, то медиана - среднее значение двух средних элементов
    else:
        return sorted_lengths[mid] # если количество элементов нечетное, то медиана - средний элемент

def sort_by_median_length(strings): #медиана длин строк
    median = median_length(strings)
    # lambda - анонимная ф-ия
    return sorted(strings, key=lambda x: (abs(len(x) - median), x)) # Lambda-функция принимает аргумент x и возвращает кортеж,
    # содержащий разницу между длиной строки x и медианой

# В порядке увеличения квадратичного отклонения между наибольшим
# ASCII-кодом символа строки и разницы в ASCII-кодах пар зеркально
# расположенных символов строки (относительно ее середины).

# ord - числовое представление символа в коде Unicode или ASCII.
def square_deviation(string):
    mid = len(string) // 2 # середина строки
    # макс код символа строки
    max_ascii = max(ord(char) for char in string)
    # список разницы в кодах пар зеркально расположенных символов относительно середины строки
    mirror_pairs = [abs(ord(string[i]) - ord(string[-i - 1])) for i in range(mid)]
    # квадратичное отклонение
    deviation = sum((pair - max_ascii) ** 2 for pair in mirror_pairs)

    print( f"Строка: {string}, Максимальный ASCII-код: {max_ascii}, Зеркальные пары: {mirror_pairs}, Отклонение: {deviation}")
    return deviation

def sort_by_deviation(strings):
    return sorted(strings, key=square_deviation)

#В порядке увеличение встречаемости самого распространенного символа
# в наборе строк от частоты его встречаемости в данной строке.

def max_char_count(string):
    # вычисления частоты наиболее часто встречающегося символа в строке
    max_char = max(set(string), key=string.count)
    return string.count(max_char)
def sort_by_frequency(strings):
    # cортировки строк по частоте наличия наиболее часто встречающегося символа.
    sorted_strings = sorted(strings, key=max_char_count)
    return sorted_strings

print("Выберите задачу:")
print("1. Отсортировать: В порядке увеличения среднего веса ASCII-кода символа строки.")
print("2. Отсортировать: В порядке увеличения медианного значения выборки строк.")
print("3. Отсортировать: В порядке увеличения квадратичного отклонения между наибольшим ASCII-кодом символа строки и разницы в ASCII-кодах пар зеркально расположенных символов (относительно ее середины).")
print("4. Остортировать: В порядке увеличение встречаемости самого распространенного символа в наборе строк от частоты его встречаемости в данной строке.")
choice = input("Введите номер задачи: ")

if choice == '1':
    print("Введите строку: ", end="")
    input_string = input()
    strings = input_string.split()
    sorted_strings = sort_by_average_weight(strings)
    print("Отсортированные в порядке увеличения среднего веса ASCII-кода символа строки. :", ' '.join(sorted_strings))
elif choice == '2':
    print("Введите строку: ", end="")
    input_string = input()
    strings = input_string.split()
    sorted_strings = sort_by_median_length(strings)
    print("Отсортированные в порядке увеличения медианного значения выборки строк:", ' '.join(sorted_strings))
elif choice == '3':
    print("Введите строки через пробел: ", end="")
    input_string = input()
    strings = input_string.split()
    sorted_strings = sort_by_deviation(strings)
    print("Отсортированные в порядке увеличения квадратичного отклонения между наибольшим ASCII-кодом символа строки и разницы в ASCII-кодах пар зеркально расположенных символов (относительно ее середины):", ' '.join(sorted_strings))
elif choice == '4':
    print("Введите строки через пробел: ", end="")
    input_string = input()
    strings = input_string.split()
    sorted_strings = sort_by_frequency(strings)
    print("Отсортированные в порядке увеличения встречаемости самого распространенного символа в наборе строк от частоты его встречаемости в данной строке:",' '.join(sorted_strings))