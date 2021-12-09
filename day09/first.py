with open("input.txt") as inp:
    topography = [list(map(int, row[:-1])) for row in inp.readlines()]

directions = {
    (1, 0), (0, 1), (-1, 0), (0, -1)
}

length = len(topography)
width = len(topography[0])
sum_risk = 0
low_points = [] # for part 2

for y in range(length):
    for x in range(width):
        is_lowest = True
        current_level = topography[y][x]
        for direction in directions:
            new_y = direction[1] + y
            new_x = direction[0] + x
            if new_y < 0 or new_x < 0 or new_y >= length or new_x >= width:
                continue
            if topography[new_y][new_x] <= current_level:
                is_lowest = False
                break
        if is_lowest:
            low_points.append((x, y))
            sum_risk += current_level + 1

print(sum_risk)
