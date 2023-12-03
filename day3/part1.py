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

    def _is_adjacent(self) -> bool:
        for x in self.xs:
            if (lines[self.y-1][x-1] != "." and not lines[self.y-1][x-1].isdigit() or
                lines[self.y-1][x] != "." and not lines[self.y-1][x].isdigit() or
                lines[self.y-1][x+1] != "." and not lines[self.y-1][x+1].isdigit() or
                lines[self.y][x-1] != "." and not lines[self.y][x-1].isdigit() or
                lines[self.y][x+1] != "." and not lines[self.y][x+1].isdigit() or
                lines[self.y+1][x-1] != "." and not lines[self.y+1][x-1].isdigit() or
                lines[self.y+1][x] != "." and not lines[self.y+1][x].isdigit() or
                lines[self.y+1][x+1] != "." and not lines[self.y+1][x+1].isdigit()):
                return True
        
        return False
    
    def getValue(self) -> int:
        if self._is_adjacent():
            return self.value
        
        return 0

n_x_lines = len(lines[0])
n_y_lines = len(lines)
lines.insert(0,'.' * n_x_lines)
lines.append('.' * n_x_lines)

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

valid_numbers = [number.getValue() for number in numbers]
print(sum(valid_numbers))

