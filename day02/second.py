with open("input.txt") as inp:
    instructions = inp.read().split('\n')[:-1]

pos = [0, 0, 0]
for instruction in instructions:
    direct, dist = instruction.split(' ')
    dist = int(dist)
    if direct[0] == 'f':
        pos[1] += dist
        pos[0] += pos[2] * dist
    elif direct[0] == 'u':
        pos[2] -= dist
    elif direct[0] == 'd':
        pos[2] += dist

print(pos[0] * pos[1])
