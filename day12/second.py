from collections import defaultdict
from first import connections


def travel_cave(cave: str, past_caves: defaultdict) -> int:
    if cave == 'end':
        return 1

    num_paths = 0
    new_history = past_caves.copy()
    new_history[cave] += 1
    if new_history[cave] >= 2 and cave.islower():
        new_history['visit_thresh'] = 1

    next_caves = set()
    for next_cave in connections[cave] - {'start'}:
        if past_caves[next_cave] < new_history['visit_thresh'] or next_cave.isupper():
            next_caves.add(next_cave)

    for new_cave in next_caves:
        num_paths += travel_cave(new_cave, new_history)
    return num_paths


travel_log = defaultdict(int)
travel_log['visit_thresh'] = 2
print(travel_cave('start', travel_log))
