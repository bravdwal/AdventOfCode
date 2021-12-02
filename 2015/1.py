def day1_ex1(instructions):
    floor = 0
    for c in instructions:
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        else:
            print(f'Found an unknown instruction: {c}')
            return
    return floor


def day1_ex2(instructions):
    floor = 0
    for idx, c in enumerate(instructions):
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        else:
            print(f'Found an unknown instruction: {c}')
            return

        if floor == -1:
            return idx + 1

    return floor


with open('files/1.txt', 'r') as f:
    instructions = f.read()

print(day1_ex1(instructions))
print(day1_ex2(instructions))
