with open("input.txt") as inp:
    dumbos = [[*map(int, row)] for row in inp.read().split('\n')[:-1]]

directions = (
    (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)
)

length = len(dumbos)
width = len(dumbos[0])
total_flashes = 0


def pretty_print():
    for row in dumbos:
        print(''.join([*map(str, row)]))


def find_flashes():
    flashes = 0
    for y in range(length):
        for x in range(width):
            if dumbos[x][y] > 9:
                dumbos[x][y] = 0
                flashes += 1
                for direction in directions:
                    new_x, new_y = x + direction[0], y + direction[1]
                    if not 0 <= new_x < width or not 0 <= new_y < length:
                        continue
                    if dumbos[new_x][new_y] != 0 and dumbos[new_x][new_y] <= 9:
                        dumbos[new_x][new_y] += 1
    return flashes


for i in range(100):
    for a in range(length):
        for b in range(width):
            dumbos[a][b] += 1
    while True:
        step_flashes = find_flashes()
        if not step_flashes:
            break
        total_flashes += step_flashes
    # print(f"Step {i + 1}:")
    # pretty_print()

print(total_flashes)
