# Отсортировать: В порядке увеличения среднего веса ASCII-кода символа строки.
def average_ascii_weight(word):
    total_weight = 0
    for char in word:
        total_weight += ord(char)
    return total_weight / len(word) if word else 0

def sort_by_average_weight(strings):
    return sorted(strings, key=average_ascii_weight)



print("Выберите задачу:")
print("1. Отсортировать: В порядке увеличения среднего веса ASCII-кода символа строки.")

choice = input("Введите номер задачи: ")

if choice == '1':
    print("Введите строку: ", end="")
    input_string = input()
    strings = input_string.split()
    sorted_strings = sort_by_average_weight(strings)
    print("Отсортированные в порядке увеличения среднего веса ASCII-кода символа строки. :", ' '.join(sorted_strings))