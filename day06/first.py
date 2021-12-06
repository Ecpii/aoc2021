with open("input.txt") as inp:
    population = map(int, inp.readline().split(','))

for i in range(80):
    new_pop = []
    for fish in population:
        if fish == 0:
            new_pop.append(6)
            new_pop.append(8)
        else:
            new_pop.append(fish - 1)
    population = new_pop

print(len(population))
