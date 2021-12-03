with open("input.txt") as inp:
    data = inp.read().split('\n')[:-1]

code_size = len(data[0])
digits = [0 for i in range(code_size)]
for code in data:
    for i in range(code_size):
        digits[i] += 1 if code[i] == '1' else -1

print(digits)

gam_rate = int(''.join(['1' if digit > 0 else '0' for digit in digits]), 2)
eps_rate = 2 ** code_size - 1 - gam_rate

print(f"{gam_rate, eps_rate}")
print(gam_rate * eps_rate)
