# Прочитать список строк с клавиатуры. Упорядочить по длине строки.

strings = []
n = int(input("Введите количество строк: "))
for i in range(n):
    string = input("Введите строку: ")
    strings.append(string)

strings.sort(key=len) # key=len параметр ф-ии в данном случае сортируем по длине

print("Упорядоченный список строк по длине:")
for string in strings:
    print(string)
