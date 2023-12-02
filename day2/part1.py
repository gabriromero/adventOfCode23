import re

def get_id_number(line: str) -> int:
    x = line.split(':')
    number = x[0].split(' ')
    return int(number[1])

def get_number_colors(line: str) -> list[tuple[int,str]]:
    x = line.split(': ')
    entries = re.split('; |, ', x[1])
    
    number_colors = []
    for entry in entries:
        x = entry.split(' ')
        number_color = (int(x[0]),x[1])
        number_colors.append(number_color)

    return number_colors

f = open("input.txt", "r")
input_lines = f.readlines()

lines = []
for input_line in input_lines:
    lines.append(str(input_line.strip()))

sum = 0
for line in lines:
    incorrect = False
    id_number = get_id_number(line)
    number_colors = get_number_colors(line)
    for number_color in number_colors:
        if (number_color[1] == 'red' and number_color[0] > 12 or 
            number_color[1] == 'green' and number_color[0] > 13 or
            number_color[1] == 'blue' and number_color[0] > 14):
            incorrect = True
            break
    
    if incorrect:
        continue
    
    sum = sum + id_number

print(sum)
