from collections import deque

with open("input.txt") as inp:
    nav_sys = inp.readlines()

openers = {'{': '}', '(': ')', '[': ']', '<': '>'}
scoring = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
syntax_score = 0
for code in nav_sys:
    closers = deque()
    for char in code:
        if char in openers:
            closers.append(openers[char])
        elif char != '\n':
            if char != closers.pop():
                syntax_score += scoring[char]
                break
print(syntax_score)
