# Дан целочисленный массив, в котором лишь один элемент отличается от остальных.
# Необходимо найти значение этого элемента.

def find_unique(arr):
    unique_element = None
    for num in arr:
        if arr.count(num) == 1:
            unique_element = num
            break
    return unique_element

print("Выберите задачу:")
print("1. Найти уникальный элемент в массиве, где все элементы, кроме одного, повторяются.")

choice = input("Введите номер задачи: ")

if choice == '1':
    print("Введите элементы массива через пробел: ", end="")
    input_array = input()
    array = list(map(int, input_array.split()))
    unique_element = find_unique(array)
    print("Уникальный элемент в массиве: ", unique_element)
