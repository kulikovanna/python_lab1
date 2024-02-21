# Дан список строк с клавиатуры. Упорядочить по количеству слов в строке.

# считаем кол-во слов в строке
def count_words(sentence):
    words = sentence.split()
    return len(words)

# сортировка списка строк по количеству слов в каждой строке
def sort_strings_by_word_count(string_list):
    return sorted(string_list, key=count_words)

strings = []
n = int(input("Введите количество строк: "))
for _ in range(n):
    strings.append(input("Введите строку: "))

sorted_strings = sort_strings_by_word_count(strings)

print("Упорядоченный список строк по количеству слов:")
for string in sorted_strings:
    print(string)
