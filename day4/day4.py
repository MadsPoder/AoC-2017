with open('input.txt', 'r') as f:
    pInput = f.read().splitlines()

#Part 1
phrases = 0
for sentences in pInput:
    sentence = sentences.split()
    if len(sentence) == len(set(sentence)):
        phrases += 1

print(phrases)