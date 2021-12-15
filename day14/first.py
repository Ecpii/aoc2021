from collections import defaultdict

with open("input.txt") as inp:
    polymer, raw_pairs = inp.read().split('\n\n')

mappings = defaultdict(str)
for raw_pair in raw_pairs.split('\n')[:-1]:
    inp_pair, spacer = raw_pair.split(' -> ')
    mappings[inp_pair] = spacer

for i in range(10):
    new_string = polymer[0]
    for j in range(len(polymer) - 1):
        new_string += mappings[polymer[j] + polymer[j + 1]] + polymer[j + 1]
    polymer = new_string


def count_polymer(chain):
    element_count = defaultdict(int)
    for element in chain:
        element_count[element] += 1

    common_count, rare_count = 0, float('inf')
    for count in element_count.values():
        if count > common_count:
            common_count = count
        if count < rare_count:
            rare_count = count
    return common_count - rare_count

print(count_polymer(polymer))