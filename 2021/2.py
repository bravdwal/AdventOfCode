import re

with open('files/2.txt', 'r') as f:
    instructions = f.readlines()

nav = [0, 0]  # position, depth
for instruction in instructions:
    if m := re.search(r'forward (\d+)', instruction):
        f, = m.groups()
        nav[0] += int(f)
    elif m := re.search(r'up (\d+)', instruction):
        u, = m.groups()
        nav[1] -= int(u)
    elif m := re.search(r'down (\d+)', instruction):
        d, = m.groups()
        nav[1] += int(d)

print(nav)
print(nav[0]*nav[1])

nav = [0, 0, 0]  # position, depth
for instruction in instructions:
    if m := re.search(r'forward (\d+)', instruction):
        f, = m.groups()
        nav[0] += int(f)
        aim = int(f)*nav[2]
        nav[1] += aim
    elif m := re.search(r'up (\d+)', instruction):
        u, = m.groups()
        # nav[1] -= int(u)
        nav[2] -= int(u)
    elif m := re.search(r'down (\d+)', instruction):
        d, = m.groups()
        # nav[1] += int(d)
        nav[2] += int(d)

print(nav)
print(nav[0]*nav[1])
