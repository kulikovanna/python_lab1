# Функция для поиска всех дат в строке в формате "день месяца год"
def find_dates(input_string):
    # делим строчку на слова
    words = input_string.split()
    dates = [] # список для хранения дат
    for word in words:
        if word.isdigit() and int(word) >= 1 and int(word) <= 31:  # смотрим является ли слово числом от 1 до 31 (день)
            # след. слово
            index = words.index(word) + 1
            if index < len(words):
                next_word = words[index]
                # смотрим является ли следующее слово названием месяца
                if next_word.lower() in ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]:
                    # проверяем следующее ли за месяцем слово годом
                    if index + 1 < len(words) and words[index + 1].isdigit() and len(words[index + 1]) == 4:  # проверяем является ли следующее слово числом из четырех цифр (год)
                        dates.append(f"{word} {next_word} {words[index + 1]}")
    return dates

input_string = "Сегодня 19 февраля 2024 года и завтра будет 20 февраля 2024"
dates = find_dates(input_string)
print("Найденные даты:", dates)
