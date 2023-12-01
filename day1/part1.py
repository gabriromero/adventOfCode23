f = open("input.txt", "r")
lines = f.readlines()

numbers = []
for line in lines:
    numbers.append(int(line))