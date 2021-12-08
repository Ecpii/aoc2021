with open("input.txt") as inp:
    data = inp.readlines()

output_sum = 0
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
display_nums = [
    {'a', 'b', 'c', 'e', 'f', 'g'},
    {'c', 'f'},
    {'a', 'c', 'd', 'e', 'g'},
    {'a', 'c', 'd', 'f', 'g'},
    {'b', 'c', 'd', 'f'},
    {'a', 'b', 'd', 'f', 'g'},
    {'a', 'b', 'd', 'e', 'f', 'g'},
    {'a', 'c', 'f'},
    {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
    {'a', 'b', 'c', 'd', 'f', 'g'}
]

for dataset in data:
    inputs, outputs = dataset[:-1].split(" | ")
    inputs = inputs.split()
    outputs = outputs.split()
    segments = {}
    inputs.sort(key=len)
    inputs = list(map(set, inputs))

    common_five = inputs[3] & inputs[4] & inputs[5]
    common_six = inputs[6] & inputs[7] & inputs[8]

    segments['a'] = inputs[1] - inputs[0]
    segments['g'] = common_six & common_five - segments['a']
    segments['d'] = common_five - segments['a'] - segments['g']
    segments['b'] = inputs[2] - inputs[0] - segments['d']

    for i in range(3, 6):
        abdg = segments['a'] | segments['b'] | segments['d'] | segments['g']
        if len(abdg & inputs[i]) == 4:  # finding display for number 5
            segments['f'] = inputs[i] - abdg

    segments['c'] = inputs[0] - segments['f']
    segments['e'] = set(letters) - segments['a'] - segments['b'] - segments['c'] - segments['d'] \
        - segments['f'] - segments['g']

    translation_set = {next(iter(v)): set(k) for k, v in segments.items()}  # reverse segments
    for i in range(4):
        translated_number = set()
        for letter in outputs[i]:
            translated_number |= translation_set[letter]
        output_sum += display_nums.index(translated_number) * (10 ** (3 - i))

print(output_sum)
