import re

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
    number_count = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    number_colors = get_number_colors(line)
    for number_color in number_colors:
        if(number_count[number_color[1]] < number_color[0]):
            number_count[number_color[1]] = number_color[0]
    
    values = list(number_count.values())
    multiply = 1
    for value in values:
        multiply = multiply * value

    sum = sum + multiply

print(sum)
