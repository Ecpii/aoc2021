from first import low_points, topography, directions, width, length

basins = []


def count_basin(coord: tuple, already_travelled: set) -> int:
    if (not 0 <= coord[1] < length)\
            or (not 0 <= coord[0] < width)\
            or topography[coord[1]][coord[0]] == 9\
            or coord in already_travelled:
        return 0

    area = 1
    for direction in directions:
        already_travelled.add(coord)
        area += count_basin((coord[0] + direction[0], coord[1] + direction[1]),
                            already_travelled)
    return area


for low_point in low_points:
    basins.append(count_basin(low_point, set()))

basins.sort(reverse=True)
basin_prod = 1
for i in range(3):
    basin_prod *= basins[i]

print(basin_prod)
