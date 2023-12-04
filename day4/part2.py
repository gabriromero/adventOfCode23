f = open("input.txt", "r")
input_lines = f.readlines()

lines = []
for input_line in input_lines:
    lines.append(str(input_line.strip()))

card_instances_dict = {}
for index, line in enumerate(lines):
    card_instances_dict[index+1] = 1

for line in lines:
    card_numbers_split = line.split(': ')
    card_id_split = [s for s in card_numbers_split[0].split(' ') if s!= '']
    card_id = int(card_id_split[1])
    numbers_split = card_numbers_split[1].split(' | ')
    winning_numbers = [int(number) for number in numbers_split[0].split(' ') if number != '']
    my_numbers = [int(number) for number in numbers_split[1].split(' ') if number != '']

    n_matches = 0
    for number in winning_numbers:
        if number in my_numbers:
            if n_matches == 0:
                n_matches = 1
            else:
                n_matches = n_matches + 1

    for i in range(card_instances_dict[card_id]):
        for i in range(card_id+1,card_id+n_matches+1):
            card_instances_dict[i] = card_instances_dict[i] + 1

print(sum(list(card_instances_dict.values())))