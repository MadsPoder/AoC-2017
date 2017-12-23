with open('input.txt', 'r') as f:
    pInput = f.read()

size = len(pInput)

#part 1
part1sum = 0
for i in range(size):
    if pInput[i] == pInput[(i+1)%size]:
        part1sum += int(pInput[i])

print(part1sum)

#part 2
offset = size/2
part2sum = 0
for i in range(size):
    if pInput[i] == pInput[(i+offset)%size]:
        part2sum += int(pInput[i])

print(part2sum)