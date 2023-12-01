f = open("input.txt", "r")
input_lines = f.readlines()

lines = []
for input_line in input_lines:
    lines.append(str(input_line))

string_numbers_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8', 
    'nine': '9'
}
sum = 0
for line in lines:
    number_found = False
    first_n = 0
    last_n = 0
    i = 0
    for char in line:
        if char.isdigit():
            if not number_found:
                number_found = True
                first_n = char
                last_n = char
            else:
                last_n = char
        
        i = i + 1
    

    sum = sum + int(first_n+last_n)
    
print(sum)