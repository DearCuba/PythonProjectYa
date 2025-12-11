"""
В этой задаче вы продолжите работать с операторами, но добавим к этому наивную сортировку данных.

Время подвести итоги гонки и объявить победителя!
Длина трассы — 43872 метра, и нам известны средние скорости трёх фаворитов: Пети, Васи и Толи.
Ваша задача — сравнить результаты гонщиков и вывести имя победителя.

Формат ввода
В первой строке записана средняя скорость Пети.
Во второй — Васи.
В третьей — Толи.

Формат вывода
Имена победителей в порядке занятых мест.
"""
petia_speed = int(input())
vasia_speed = int(input())
tolia_speed = int(input())

if tolia_speed < petia_speed > vasia_speed and vasia_speed > tolia_speed:
    print(f"1. Петя\n2. Вася\n3. Толя")
elif tolia_speed < petia_speed > vasia_speed and vasia_speed < tolia_speed:
    print(f"1. Петя\n2. Толя\n3. Вася")
elif tolia_speed < vasia_speed > petia_speed and petia_speed > tolia_speed:
    print(f"1. Вася\n2. Петя\n3. Толя")
elif tolia_speed < vasia_speed > petia_speed and petia_speed < tolia_speed:
    print(f"1. Вася\n2. Толя\n3. Петя")
elif vasia_speed < tolia_speed > petia_speed and petia_speed > vasia_speed:
    print(f"1. Толя\n2. Петя\n3. Вася")
elif vasia_speed < tolia_speed > petia_speed and petia_speed < vasia_speed:
    print(f"1. Толя\n2. Вася\n3. Петя")
