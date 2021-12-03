with open("input.txt") as inp:
    data = inp.read().split('\n')[:-1]

code_size = len(data[0])


def find_rating(oxygen=True):
    remaining_numbers = data.copy()
    for i in range(code_size):
        temp = []
        a = 0
        for number in remaining_numbers:
            a += 1 if number[i] == "1" else -1
        if oxygen:
            special_value = "1" if a >= 0 else "0"
        else:
            special_value = "0" if a >= 0 else "1"

        for number in remaining_numbers:
            if number[i] == special_value:
                temp.append(number)
        remaining_numbers = temp
        if len(remaining_numbers) == 1:
            return int(remaining_numbers[0], 2)


print(find_rating() * find_rating(False))
