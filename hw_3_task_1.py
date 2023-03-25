# 1. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите два варианта решения: через list и через dict.
#
# Пример:
# Введите номер месяца: 10
# Результат через список: Осень
# Результат через словарь: Осень

# Первый вариант решения:

# a = int(input('Choose month: '))
# if a == 1 or a == 2 or a == 12:
#     print('Winter')
# elif a == 3 or a == 4 or a == 5:
#     print('Sping')
# elif a == 6 or a == 7 or a == 8:
#     print('Summer')
# elif a == 9 or a == 10 or a == 11:
#     print('Autumn')
# else:
#     print('Error')

# Второй вариант решения:

seasons = {'Winter': (1, 2, 12),
           'Sping': (3, 4, 5),
           'Summer': (6, 7, 8),
           'Autumn': (9, 10, 11)}

month = int(input('Choose a month: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)

