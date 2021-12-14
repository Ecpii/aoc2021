with open("input.txt") as inp:
    coords, instructions = inp.read().split('\n\n')

coords = coords.split('\n')
instructions = instructions.split('\n')
paper = {}

for coord in coords:
    x, y = map(int, coord.split(','))
    paper[x, y] = True

fold_direction = instructions[0][11]
fold_pos = int(instructions[0][13:])
old_paper = paper.copy()

if fold_direction == 'x':
    for dot_x, dot_y in old_paper:
        paper[dot_x, dot_y] = False
        paper[fold_pos - abs(fold_pos - dot_x), dot_y] = True
else:

    for dot_x, dot_y in old_paper:
        paper[dot_x, dot_y] = False
        paper[dot_x, fold_pos - abs(fold_pos - dot_y)] = True

num_visible = 0
for value in paper.values():
    if value:
        num_visible += 1

print(num_visible)
