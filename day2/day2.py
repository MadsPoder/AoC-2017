from itertools import combinations

with open('input.txt', 'r') as f:
    pInput = f.read().splitlines()

spreadsheet = [list(map(int, e.split())) for e in pInput]
rows = len(spreadsheet)

#part 1
checksums = [max(e)-min(e) for e in spreadsheet]
print(sum(checksums))

#part 2
divChecksums = []

for i in range(rows):
    for a, b in combinations(spreadsheet[i], 2):
        if a % b == 0:
            divChecksums.append(a/b)
        elif b % a == 0:
            divChecksums.append(b/a)

print(sum(divChecksums))