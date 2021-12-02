def day8_ex1(lines):
    code_count = 0
    memory_count = 0
    for line in lines:
        line = line.rstrip()  # remove trailing \n
        code_count += len(line)

        s = line.decode('unicode_escape')[1:-1]  # surrounding "" are not stored in memory
        memory_count += len(s)

    return code_count, memory_count, code_count - memory_count


def day8_ex2(lines):
    code_count = 0
    memory_count = 0
    for line in lines:
        line = line.rstrip()  # remove trailing \n
        code_count += len(line)

        s = str(line)[2:-1]  # remove surrounding b''
        r = ''
        for c in s:
            if c == '\"':
                r = rf'{r}\"'
            else:
                r = rf'{r}{c}'
        memory_count += len(r) + 2   # take the extra surrounding "" into account

    return code_count, memory_count, memory_count - code_count


with open('files/8.txt', 'rb') as f:
    lines = f.readlines()

with open('files/8_test.txt', 'rb') as f:
    lines_test = f.readlines()

print('Check for ex1')
print('-------------')
print(day8_ex1(lines_test), '\n')

print('Result of ex1')
print('-------------')
print(day8_ex1(lines), '\n')

print('Check for ex2')
print('-------------')
print(day8_ex2(lines_test), '\n')

print('Result of ex2')
print('-------------')
print(day8_ex2(lines), '\n')
