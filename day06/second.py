with open("input.txt") as inp:
    population = map(int, inp.readline().split(','))

timer_nums = [0 for i in range(9)]
for fish in population:
    timer_nums[fish] += 1

for i in range(256):
    births = timer_nums[0]
    for j in range(8):
        timer_nums[j] = timer_nums[j + 1]
    timer_nums[6] += births
    timer_nums[8] = births

print(sum(timer_nums))
