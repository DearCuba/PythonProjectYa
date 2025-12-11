"""
Кто пойдёт первым? В настольных играх очередность часто определяется жребием, но мы будем использовать порядок букв!

Давайте сравним имена игроков лексикографически и с помощью условных операторов определим, кто начнёт игру.

Формат ввода
Три имени игроков, каждое из которых записано с новой строки.

Формат вывода
Имя игрока, который будет ходить первым.
"""
player_one = input()
player_two = input()
player_three = input()

player_one_first_letter = player_one[0]
player_two_first_letter = player_two[0]
player_three_first_letter = player_three[0]

nummber_first_letter_winner = (min(ord(player_one_first_letter), ord(player_two_first_letter),
                                   ord(player_three_first_letter)))

if nummber_first_letter_winner == ord(player_one_first_letter):
    print(player_one)
elif nummber_first_letter_winner == ord(player_two_first_letter):
    print(player_two)
elif nummber_first_letter_winner == ord(player_three_first_letter):
    print(player_three)