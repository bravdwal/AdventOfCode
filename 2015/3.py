with open('files/3.txt', 'r') as f:
    navigations = f.read()


def day3(navigations, num_santas=1):
    keys = [[0, 0] for _ in range(num_santas)]
    deliveries = {tuple(keys[0]): num_santas}

    # If the number of santas is not a divider of the number of instructions,
    # then we put some santas to rest at the end (by introducing the '.' instruction)
    if (diff := len(navigations) % num_santas) != 0:
        n = num_santas - diff
        s = ['.' for _ in range(n)]
        navigations += ''.join(s)

    print(f'num_santas={num_santas}, len(navigations)={len(navigations)}')

    for idx in range(0, len(navigations), num_santas):
        for p in range(num_santas):
            n = navigations[idx+p]
            if n == '^':
                keys[p][0] += 1
            elif n == '>':
                keys[p][1] += 1
            elif n == 'v':
                keys[p][0] -= 1
            elif n == '<':
                keys[p][1] -= 1
            elif n == '.':
                pass
            else:
                print(f'Found an unkown instruction: {n}')
                return

            if (k := tuple(keys[p])) not in deliveries:
                deliveries[k] = 0
            deliveries[k] += 1

    return len(deliveries)


print(day3(navigations, num_santas=1))
print(day3(navigations, num_santas=2))
print(day3(navigations, num_santas=3))
print(day3(navigations, num_santas=4))
print(day3(navigations, num_santas=5))
print(day3(navigations, num_santas=6))
