with open("input.txt") as inp:
    positions = list(map(int, inp.readline().split(",")))

positions.sort()
middle = int((len(positions) - 1) / 2)
if len(positions) % 2:
    optimal_pos = positions[middle]
else:
    optimal_pos = round((positions[middle] + positions[middle + 1]) / 2)

fuel_used = 0
for position in positions:
    fuel_used += abs(optimal_pos - position)

print(fuel_used)
