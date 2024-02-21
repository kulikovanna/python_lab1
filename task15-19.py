# Дан целочисленный массив, в котором лишь один элемент отличается от остальных.
# Необходимо найти значение этого элемента.

def find_unique(arr):
    unique_element = None
    for num in arr:
        if arr.count(num) == 1:
            unique_element = num
            break
    return unique_element

# Дан целочисленный массив. Необходимо найти два наименьших элемента.

def find_two_smallest(arr):
    sorted_arr = sorted(arr)
    return sorted_arr[:2]

print("Выберите задачу:")
print("1. Найти уникальный элемент в массиве, где все элементы, кроме одного, повторяются.")
print("2. Дан целочисленный массив. Необходимо найти два наименьших элемента.")

choice = input("Введите номер задачи: ")

if choice == '1':
    print("Введите элементы массива через пробел: ", end="")
    input_array = input()
    array = list(map(int, input_array.split()))
    unique_element = find_unique(array)
    print("Уникальный элемент в массиве: ", unique_element)
elif choice == '2':
    print("Введите элементы массива через пробел: ", end="")
    input_array = input()
    array = list(map(int, input_array.split()))
    two_smallest_elements = find_two_smallest(array)
    print("Два наименьших элемента в массиве:", ' '.join(map(str, two_smallest_elements)))