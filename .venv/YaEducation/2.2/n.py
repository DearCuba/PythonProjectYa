"""
Во времена, когда люди верили в магическую силу чисел, волшебник Пифуман предал все народы и встал на сторону Зерона.

Теперь, чтобы проникнуть в башни обоих злодеев одновременно, нужно разделить силу числа, которое защищало нас в дороге.

Для этого возьмём трёхзначное число и составим из него минимальное и максимальное возможные двухзначные числа.

Формат ввода
Одно трёхзначное число.

Формат вывода
Два защитных числа для каждого отряда, записанные через пробел.
"""
number = int(input())

# разделяем число на цифры
first_digit = number // 100
second_digit = number // 10 % 10
third_digit = number % 10

# находим первую цифру масимального двузначного числа
if first_digit >= second_digit and first_digit >= third_digit:
    max_max = first_digit
elif second_digit >= first_digit and second_digit >= third_digit:
    max_max = second_digit
else:
    max_max = third_digit

# находим вторую цифру масимального двузначного числа
if first_digit >= second_digit and first_digit <= third_digit:
    min_max = first_digit
elif first_digit <= second_digit and first_digit >= third_digit:
    min_max = first_digit
elif second_digit >= first_digit and second_digit <= third_digit:
    min_max = second_digit
elif second_digit <= first_digit and second_digit >= third_digit:
    min_max = second_digit
else:
    min_max = third_digit

# находим первую цифру минимального двузначного числа
if first_digit >= second_digit and first_digit <= third_digit:
    min_max = first_digit
elif first_digit <= second_digit and first_digit >= third_digit:
    min_max = first_digit
elif second_digit >= first_digit and second_digit <= third_digit:
    min_max = second_digit
elif second_digit <= first_digit and second_digit >= third_digit:
    min_max = second_digit
else:
    min_max = third_digit

# находим вторую цифру минимального двузначного числа
if first_digit <= second_digit and first_digit <= third_digit:
    min_min = first_digit
elif second_digit <= first_digit and second_digit <= third_digit:
    min_min = second_digit
else:
    min_min = third_digit

# выводим числа в порядке указанном в задании
if min_max == 0 and min_min == 0:
    print(f"{max_max}{min_max} {max_max}{min_max}")
elif min_min == 0:
    print(f"{min_max}{min_min} {max_max}{min_max}")
else:
    print(f"{min_min}{min_max} {max_max}{min_max}")