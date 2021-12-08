with open("input.txt") as inp:
    data = inp.readlines()

num_easy_digits = 0

for dataset in data:
    outputs = dataset[:-1].split(" | ")[1].split()
    for output in outputs:
        if len(output) in {2, 3, 4, 7}:
            num_easy_digits += 1

print(num_easy_digits)
