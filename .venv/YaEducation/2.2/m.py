"""
Отлично! Давайте теперь закрепим навык работы с условным оператором if-else и ещё раз выделим отдельные цифры числа.

Во времена магии и драконов ходили легенды о числах, обладающих великой силой, способной изменить мир.

Три числа были даны эльфам, семь — гномам, а девять достались человеческому роду.

Но все они были обмануты... Потому что существовало ещё одно число. В стране Нумия, на бумаге из тёмного папируса,
властелин Зерон тайно записал Единую Цифру, подчиняющую себе все великие числа.

Давайте выясним, что это за цифра!

Формат ввода
В первой строке записано двузначное число одного из эльфов.
Во второй строке — Гномов.
В третьей — Людей.

Формат вывода
Одна цифра — общая у всех трёх чисел в одинаковой позиции
"""
elves_number = int(input())
dwarves_number = int(input())
peoples_number = int(input())

first_digit_elves = int(elves_number // 10)
second_digit_elves = int(elves_number % 10)

first_digit_dwarves = int(dwarves_number // 10)
second_digit_dwarves = int(dwarves_number % 10)

first_digit_peoples = int(peoples_number // 10)
second_digit_peoples = int(peoples_number % 10)

if first_digit_elves == first_digit_dwarves == first_digit_peoples:
    print(first_digit_elves)

if second_digit_elves == second_digit_dwarves == second_digit_peoples:
    print(second_digit_elves)