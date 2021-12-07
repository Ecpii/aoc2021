with open("input.txt") as inp:
    positions = list(map(int, inp.readline().split(",")))

optimal_pos = int(sum(positions) / len(positions))

fuel_used = [0, 0]
for i in range(2):  # loops to catch number above and below
    for position in positions:
        dist = abs(optimal_pos + i - position)
        fuel_used[i] += (dist + 1) * dist / 2

print(min(fuel_used))
