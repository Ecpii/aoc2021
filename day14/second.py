from first import count_polymer
with open("example.txt") as inp:
    polymer, raw_pairs = inp.read().split('\n\n')

mappings = {}
for raw_pair in raw_pairs.split('\n')[:-1]:
    inp_pair, spacer = raw_pair.split(' -> ')
    mappings[inp_pair] = {0: inp_pair, 1: inp_pair[0] + spacer + inp_pair[1]}


def advance_polymer(comp: str, steps: int) -> str:
    """
    The main function to advance the polymer using the mappings dictionary. Does memorization in
    said dictionary, and is recursive.
    :param comp: the starting polymer
    :param steps: how many steps to advance the polymer
    :return: the state of the polymer after steps number of steps
    """
    if len(comp) == 2:
        if steps not in mappings[comp]:
            mappings[comp][steps] = advance_polymer(mappings[comp][1], steps - 1)
        return mappings[comp][steps]

    new_polymer = comp[0]
    for i in range(len(comp) - 1):
        new_polymer += advance_polymer(comp[i:i + 2], steps)[1:]

    return new_polymer


output = advance_polymer(polymer, 40)
# print(mappings)
print(count_polymer(output))
