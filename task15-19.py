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

# Дано вещественное число R и массив вещественных чисел.
# Найти элемент массива, который наиболее близок к данному числу.

def find_closest(arr, R):
    closest_element = arr[0]
    smallest_diff = abs(arr[0] - R)
    for element in arr:
        current_diff = abs(element - R)
        if current_diff < smallest_diff:
            closest_element = element
            smallest_diff = current_diff
    return closest_element

# Для введенного списка положительных чисел построить список всех положительных делителей элементов списка без повторений.

def positive_divisors(numbers):
    all_divisors = []
    for num in numbers:
        num_divisors = [] # делители текущего числа
        for i in range(1, num + 1):
            if num % i == 0:
                num_divisors.append(i)
        # добавляем список делителей num в общий список всех делителей
        all_divisors.extend(num_divisors)

    # преобразуем список всех делителей во мн-во, чтобы убрать повторяющиеся элементы,
    # а затем преобразуем его обратно в список и возвр результат
    return list(set(all_divisors))

print("Выберите задачу:")
print("1. Найти уникальный элемент в массиве, где все элементы, кроме одного, повторяются.")
print("2. Дан целочисленный массив. Необходимо найти два наименьших элемента.")
print("3. Найти элемент массива, наиболее близкий к заданному числу R.")
print("4. Найти все положительные делители элементов списка.")

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
elif choice == '3':
    R = float(input("Введите число R: "))
    print("Введите элементы массива через пробел: ", end="")
    input_array = input()
    array = list(map(float, input_array.split()))
    closest_element = find_closest(array, R)
    print(f"Элемент, наиболее близкий к {R}: {closest_element}")
elif choice == '4':
    print("Введите элементы списка через пробел: ", end="")
    input_numbers = input()
    numbers = list(map(int, input_numbers.split()))
    divisors = positive_divisors(numbers)
    print("Положительные делители элементов списка без повторений:", divisors)