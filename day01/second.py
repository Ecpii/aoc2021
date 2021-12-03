with open("input.txt") as inp:
    depths = list(map(int, inp.read().split('\n')[:-1]))

num_increases = 0
prev_sum = sum(depths[0:3])
for i in range(3, len(depths)):
    new_sum = prev_sum - depths[i - 3] + depths[i]
    if new_sum > prev_sum:
        num_increases += 1
    prev_sum = new_sum

print(num_increases)
