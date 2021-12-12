from first import dumbos, find_flashes

length = len(dumbos)
width = len(dumbos[0])
step_num = 0


def all_flashed():
    for row in dumbos:
        for num in row:
            if num:
                return False
    return True


while not all_flashed():
    step_num += 1
    for a in range(length):
        for b in range(width):
            dumbos[a][b] += 1
    while find_flashes():
        pass

print(step_num + 100)
