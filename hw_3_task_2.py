# 2. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль (try except).
#
# Пример:
# Введите первое число: 10
# Введите второе число: 0
# Вы что? Пытаетесь делить на 0!
#
# Process finished with exit code 0
#
# Пример:
# Введите первое число: 10
# Введите второе число: 10
# 1.0
#
# Process finished with exit code 0

def my_func(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "you cannot divide by zero"
    except ValueError:
        return "you have entered a wrong symbol, integer needed"


print(my_func(int(input("Enter x = ")), int(input("Enter y = "))))
