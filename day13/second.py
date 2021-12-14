from collections import defaultdict

with open("input.txt") as inp:
    coords, instructions = inp.read().split('\n\n')

coords = coords.split('\n')
instructions = instructions.split('\n')[:-1]
paper = defaultdict(bool)

for coord in coords:
    x, y = map(int, coord.split(','))
    paper[x, y] = True

for instruction in instructions:

    fold_direction = instruction[11]
    fold_pos = int(instruction[13:])
    old_paper = paper.copy()

    for dot_x, dot_y in old_paper:
        paper[dot_x, dot_y] = False
        if fold_direction == 'x':
            paper[fold_pos - abs(fold_pos - dot_x), dot_y] = True
        else:
            paper[dot_x, fold_pos - abs(fold_pos - dot_y)] = True

max_x, max_y = 0, 0
for coord, mark in paper.items():
    if coord[0] > max_x and mark:
        max_x = coord[0]
    if coord[1] > max_y and mark:
        max_y = coord[1]

for m in range(max_y + 1):
    for n in range(max_x + 1):
        print('#' if paper[n, m] else ' ', end='')
    print()
