# TODO Напишите функцию find_common_participants
def find_common_participants(group_1, group_2, sep = ','):
    group_1 = group_1.split(sep)
    group_2 = group_2.split(sep)
    common = set(group_1).intersection(group_2)
    return sorted(common)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group)
print(common_participants)
