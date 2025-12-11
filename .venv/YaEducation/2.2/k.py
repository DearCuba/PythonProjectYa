"""
Согласно одному древнему поверью, трёхзначное число считается красивым, если сумма его минимальной и максимальной цифр
равна оставшейся цифре умноженной на 2.

Напишите программу, которая проверяет, является ли число красивым.

Формат ввода
Одно трёхзначное число

Формат вывода
YES — если число красивое, иначе — NO
"""
number = int(input())

first_digit = int(number // 100)
second_digit = number // 10 % 10
third_digit = number % 10

max_digit = max(first_digit, second_digit, third_digit)
mid_digit = int(0)
min_digit = int(min(first_digit, second_digit, third_digit))

if first_digit != min_digit and first_digit != max_digit:
    mid_digit = first_digit
elif second_digit != max_digit and second_digit != min_digit:
    mid_digit = second_digit
else:
    mid_digit = third_digit

if max_digit + min_digit == mid_digit * 2:
    print('YES')
else:
    print('NO')
