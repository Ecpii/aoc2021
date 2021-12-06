from collections import defaultdict
# from first import pretty_print

with open("input.txt") as inp:
    lines = inp.read().split('\n')[:-1]

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
    else:
        x_inc = -1 if end_coords[0] < start_coords[0] else 1
        y_inc = -1 if end_coords[1] < start_coords[1] else 1
        for i in range(abs(start_coords[0] - end_coords[0]) + 1):
            points[(start_coords[0] + i * x_inc, start_coords[1] + i * y_inc)] += 1

num_danger_points = 0
for fissures in points.values():
    if fissures >= 2:
        num_danger_points += 1

# pretty_print(points)
print(num_danger_points)
