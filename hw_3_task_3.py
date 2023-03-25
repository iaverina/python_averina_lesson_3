# 3. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания,email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
#
# Пример:
# Иван Иванов 1846 года рождения, проживает в городе Москва,
# email: jackie@gmail.com, телефон: 01005321456

user_name = str(input("Input name: "))
user_surname = str(input("Input surname: "))
user_year = str(input("Input year: "))
user_city = str(input("Input city: "))
user_email = str(input("Input email: "))
user_phone = str(input("Input phone: "))


def personal_info(user_name, user_surname, user_year, user_city, user_email,
                  user_phone):
    return ' '.join([
        "name:", user_name,
        ", surname:", user_surname,
        ", year:", user_year,
        ", city:", user_city,
        ", email:", user_email,
        ", phone:", user_phone, "."
    ])


print(personal_info(user_name, user_surname, user_year, user_city, user_email,
                    user_phone))
