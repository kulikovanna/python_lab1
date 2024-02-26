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


print("Выберите задачу:")
print("1. Отсортировать: В порядке увеличения среднего веса ASCII-кода символа строки.")
print("2. Отсортировать: В порядке увеличения медианного значения выборки строк.")

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