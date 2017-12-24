with open('input.txt', 'r') as f:
    pInput = f.read().splitlines()

#Part 1
instructions = [int(e) for e in pInput]

idx = 0
steps = 0
while idx in range(0,len(instructions)):
    steps += 1
    temp = instructions[idx]
    instructions[idx] += 1
    idx = idx + temp

print(steps)

#Part 2
instructions = [int(e) for e in pInput]

idx = 0
steps = 0
while idx in range(0,len(instructions)):
    steps += 1
    temp = instructions[idx]
    instructions[idx] = temp - 1 if instructions[idx] >= 3 else temp + 1
    idx = idx + temp

print(steps)