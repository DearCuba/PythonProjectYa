"""
Ура! Зерон повержен, и это всё благодаря вам! Герои заслужили отдых. Сделайте короткую паузу, чтобы восстановить силы,
и возвращайтесь, когда будете готовы.

Осталось ещё 4 задачи! Давайте освежим в памяти, как работать с вложенными условными операторами if-else или
if-elif-else и применять наивную сортировку данных.

В новом сезоне за первенство в велогонках снова сражаются сильнейшие. Протяжённость финальной трассы — 43872м,
и все хотят узнать, кто первым пересечёт финишную черту.

Нам известны средние скорости трёх претендентов — Пети, Васи и Толи. Кто станет победителем?

Формат ввода
В первой строке записана средняя скорость Пети.
Во второй — Васи.
В третьей — Толи.

Формат вывода
Красивый пьедестал (ширина ступеней 8 символов).
"""

petia = 'Петя'
vasia = 'Вася'
tolia = 'Толя'

petia_average_speed = int(input())
vasia_average_speed = int(input())
tolia_average_speed = int(input())

# petia first
if (petia_average_speed > vasia_average_speed and petia_average_speed > tolia_average_speed and
        vasia_average_speed > tolia_average_speed):
    place_1 = petia
    place_2 = vasia
    place_3 = tolia
elif (petia_average_speed > vasia_average_speed and petia_average_speed > tolia_average_speed and
      tolia_average_speed > vasia_average_speed):
    place_1 = petia
    place_2 = tolia
    place_3 = vasia

# vasia first
elif (vasia_average_speed > petia_average_speed and vasia_average_speed > tolia_average_speed and
      petia_average_speed > tolia_average_speed):
    place_1 = vasia
    place_2 = petia
    place_3 = tolia
elif (vasia_average_speed > petia_average_speed and vasia_average_speed > tolia_average_speed and
      tolia_average_speed > petia_average_speed):
    place_1 = vasia
    place_2 = tolia
    place_3 = petia

# tolia first
elif (tolia_average_speed > petia_average_speed and tolia_average_speed > vasia_average_speed and
      vasia_average_speed > petia_average_speed):
    place_1 = tolia
    place_2 = vasia
    place_3 = petia
elif (tolia_average_speed > petia_average_speed and tolia_average_speed > vasia_average_speed and
      petia_average_speed > vasia_average_speed):
    place_1 = tolia
    place_2 = petia
    place_3 = vasia

# вывод результатов гонки
print(f"          {place_1}          ")
print(f"  {place_2}                  ")
print(f"                  {place_3}  ")
print(f"   II      I      III   ")



# print ('__________Толя__________')
# print ('__Вася__________________')
# print ('__________________Петя__')
# print ('___II______I______III___')
# print ('          Толя          ')
# print ('  Вася                  ')
# print ('                  Петя  ')
# print ('   II      I      III   ')