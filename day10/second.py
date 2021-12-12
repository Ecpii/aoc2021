from collections import deque

with open("input.txt") as inp:
    nav_sys = inp.readlines()

openers = {'{': '}', '(': ')', '[': ']', '<': '>'}
scoring = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
scores = []
for code in nav_sys:
    syntax_score = 0
    closers = deque()
    line_corrupted = False
    for char in code:
        if char in openers:
            closers.appendleft(openers[char])
        elif char != '\n':
            if char != closers.popleft():
                line_corrupted = True
                break
    if not line_corrupted:
        for closer in closers:
            syntax_score *= 5
            syntax_score += scoring[closer]
        scores.append(syntax_score)

scores.sort()
print(scores[len(scores) // 2])
