list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
half_num_players = len(list_players) // 2
first = list_players[:half_num_players]
second = list_players[half_num_players:]
print(first)
print(second)
