with open("input.txt") as inp:
    prev_depth, *depths = map(int, inp.read().split('\n')[:-1])

num_increases = 0
print(f"{prev_depth = }")
print(f"{depths = }")
for depth in depths:
    if depth > prev_depth:
        num_increases += 1
    prev_depth = depth
print(num_increases)
