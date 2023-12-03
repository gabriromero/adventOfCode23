f = open("input.txt", "r")
input_lines = f.readlines()

lines = []
for input_line in input_lines:
    lines.append(str(input_line.strip()))

class Number:
    def __init__(self, y: int, xs: list[int], value: int):
        self.data = []
        self.y = y
        self.xs = xs
        self.value = value

    def exists(self, x: int, y: int) -> bool:
        return x in self.xs and y == self.y
    
    def getValue(self) -> int:
        return self.value

def findNumber(x: int, y: int):
    for number in numbers:
        if number.exists(x,y):
            return number.getValue()
    
    return 0

def checkGearRatio(x: int, y: int) -> int:
    numbersFound = set()
    squares = [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]
    for square in squares:
        value = findNumber(square[0],square[1])
        if value > 0:
            numbersFound.add(value)
    
    if len(numbersFound) == 2:
        l = list(numbersFound)
        return (l[0] * l[1])
    
    return 0


n_x_lines = len(lines[0])
n_y_lines = len(lines)
lines.insert(0,'.' * n_x_lines)
lines.append('.' * n_x_lines)
_sum = 0

for i in range(len(lines)):
    lines[i] = '.' + lines[i] + '.'

numbers = []
for y_index, line in enumerate(lines):
    xs = []
    for x_index, char in enumerate(line):
        if char.isdigit():
            xs.append(x_index)
        
        else:
            if len(xs) > 0:
                number = Number(y_index,xs,int("".join(line[x_index-len(xs):x_index])))
                numbers.append(number)
                xs = []

for y_index, line in enumerate(lines):
    for x_index, char in enumerate(line):
        if char == "*":
            _sum = _sum + checkGearRatio(x_index, y_index)

print(_sum)

