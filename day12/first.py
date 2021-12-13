from collections import defaultdict

with open("input.txt") as inp:
    cave_map = inp.read().split('\n')[:-1]

connections = defaultdict(set)

for connection in cave_map:
    parts = connection.split('-')
    connections[parts[0]].add(parts[1])
    connections[parts[1]].add(parts[0])


def travel_cave(cave: str, past_caves: set) -> int:
    if cave == 'end':
        return 1
    next_caves = connections[cave] - past_caves
    num_paths = 0
    for new_cave in next_caves:
        num_paths += travel_cave(new_cave,
                                 past_caves if cave.isupper() else past_caves | {cave})
    return num_paths


print(travel_cave('start', set()))
