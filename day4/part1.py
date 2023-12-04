f = open("input.txt", "r")
input_lines = f.readlines()

lines = []
for input_line in input_lines:
    lines.append(str(input_line.strip()))

sum = 0
for line in lines:
    card_numbers_split = line.split(': ')
    card_id_split = card_numbers_split[0].split(' ')
    card_id = card_id_split[1]
    numbers_split = card_numbers_split[1].split(' | ')
    winning_numbers = [int(number) for number in numbers_split[0].split(' ') if number != '']
    my_numbers = [int(number) for number in numbers_split[1].split(' ') if number != '']

    points = 0
    for number in winning_numbers:
        if number in my_numbers:
            if points == 0:
                points = 1
            else:
                points = points * 2

    sum = sum + points
    
print(sum)