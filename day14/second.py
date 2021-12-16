from collections import Counter

with open("input.txt") as inp:
    polymer, pairings = inp.read().split('\n\n')

mappings = {}
for pairing in pairings.split('\n')[:-1]:
    elem_pair, insertion = pairing.split(' -> ')
    mappings[elem_pair] = [
        {1: Counter(insertion)},  # dict of memorized counts
        elem_pair[0] + insertion,  # child pair
        insertion + elem_pair[1]  # child pair
    ]
element_count = Counter(polymer)


def run_polymer(pair: str, steps: int) -> Counter:
    if steps not in mappings[pair][0]:
        mappings[pair][0][steps] = mappings[pair][0][1] \
            + run_polymer(mappings[pair][1], steps - 1) \
            + run_polymer(mappings[pair][2], steps - 1)

    return mappings[pair][0][steps]


for i in range(len(polymer) - 1):
    element_count += run_polymer(polymer[i] + polymer[i + 1], 40)

print(element_count.most_common(1)[0][1] - element_count.most_common()[-1][1])
