"""
До победы над злом остался последний шаг — разрушить логово Зерона.

Для этого нам нужно создать трёхзначное магическое число, которое будет сильнее двух защитных чисел Зерона.

Как его составить?

Первая цифра — максимальная из всех защитных чисел.
Последняя цифра — минимальная.
Средняя цифра — сумма оставшихся цифр без учёта переноса разряда.

Соберите это магическое число и помогите одолеть зло!

Формат ввода
В двух строках записаны защитные числа Зерона.

Формат вывода
Одно трёхзначное число, которое приведёт к победе.
"""
num_one = int(input())
num_two = int(input())

# разделяем оба введеных числа на цифры
first_num = num_one // 10 % 10
second_num = num_one % 10
third_num = num_two // 10 % 10
fourth_num = num_two % 10

# определяем первую и вторую цифру магического числа, а так же сумму оставшихся
# if first_num = MAX
if (first_num >= second_num and first_num >= third_num and first_num >= fourth_num and second_num <= first_num and
        second_num <= third_num and second_num <= fourth_num):
    max_num = first_num
    min_num = second_num
    sum = (third_num + fourth_num) % 10

elif (first_num >= second_num and first_num >= third_num and first_num >= fourth_num and third_num <= first_num and
      third_num <= second_num and third_num <= fourth_num):
    max_num = first_num
    min_num = third_num
    sum = (second_num + fourth_num) % 10

elif (first_num >= second_num and first_num >= third_num and first_num >= fourth_num and fourth_num <= first_num and
      fourth_num <= second_num and fourth_num <= third_num):
    max_num = first_num
    min_num = fourth_num
    sum = (second_num + third_num) % 10

# if second_num = MAX
elif (second_num >= first_num and second_num >= third_num and second_num >= fourth_num and first_num <= second_num and
      first_num <= third_num and first_num <= fourth_num):
    max_num = second_num
    min_num = first_num
    sum = (third_num + fourth_num) % 10

elif (second_num >= first_num and second_num >= third_num and second_num >= fourth_num and third_num <= first_num and
      third_num <= second_num and third_num <= fourth_num):
    max_num = second_num
    min_num = third_num
    sum = (first_num + fourth_num) % 10

elif (second_num >= first_num and second_num >= third_num and second_num >= fourth_num and fourth_num <= first_num and
      fourth_num <= second_num and fourth_num <= third_num):
    max_num = second_num
    min_num = fourth_num
    sum = (first_num + third_num) % 10

# if third_num = MAX
elif (third_num >= first_num and third_num >= second_num and third_num >= fourth_num and first_num <= second_num and
      first_num <= third_num and first_num <= fourth_num):
    max_num = third_num
    min_num = first_num
    sum = (second_num + fourth_num) % 10

elif (third_num >= first_num and third_num >= second_num and third_num >= fourth_num and second_num <= first_num and
      second_num <= third_num and second_num <= fourth_num):
    max_num = third_num
    min_num = second_num
    sum = (first_num + fourth_num) % 10

elif (third_num >= first_num and third_num >= second_num and third_num >= fourth_num and fourth_num <= first_num and
      fourth_num <= second_num and fourth_num <= third_num):
    max_num = third_num
    min_num = fourth_num
    sum = (first_num + second_num) % 10

# if fourth_num = MAX
elif (fourth_num >= first_num and fourth_num >= second_num and fourth_num >= third_num and first_num <= second_num and
      first_num <= third_num and first_num <= fourth_num):
    max_num = fourth_num
    min_num = first_num
    sum = (second_num + third_num) % 10

elif (fourth_num >= first_num and fourth_num >= second_num and fourth_num >= third_num and second_num <= first_num and
      second_num <= third_num and second_num <= fourth_num):
    max_num = fourth_num
    min_num = second_num
    sum = (first_num + third_num) % 10

elif (fourth_num >= first_num and fourth_num >= second_num and fourth_num >= third_num and third_num <= first_num and
      third_num <= second_num and third_num <= fourth_num):
    max_num = fourth_num
    min_num = third_num
    sum = (first_num + second_num) % 10

# собираем магическое число
print(f"{max_num}{sum}{min_num}")