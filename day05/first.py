from collections import defaultdict

with open("input.txt") as inp:
    lines = inp.read().split('\n')[:-1]


def pretty_print(fissure_points):
    max_x, max_y = 0, 0
    for point in fissure_points:
        if point[0] > max_x:
            max_x = point[0]
        if point[1] > max_y:
            max_y = point[1]

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            num_fissures = fissure_points[x, y]
            print('.' if not num_fissures else num_fissures, end="")
        print()


points = defaultdict(int)

for line in lines:
    start, end = line.split(" -> ")
    start_coords = tuple(map(int, start.split(',')))
    end_coords = tuple(map(int, end.split(',')))
    if start_coords[0] == end_coords[0]:
        for i in range(min(start_coords[1], end_coords[1]), max(start_coords[1], end_coords[1]) + 1):
            points[(start_coords[0], i)] += 1
    elif start_coords[1] == end_coords[1]:
        for i in range(min(start_coords[0], end_coords[0]), max(start_coords[0], end_coords[0]) + 1):
            points[(i, start_coords[1])] += 1

num_danger_points = 0
for fissures in points.values():
    if fissures >= 2:
        num_danger_points += 1

# pretty_print(points)
print(num_danger_points)
