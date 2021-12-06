def fish_after_days(fish, days):
    for _ in range(days):
        zfish = fish[0]
        fish = {k-1: fish[k] for k in range(1, 9)}
        fish[6] += zfish
        fish[8] = zfish
    return sum(fish.values())


with open('files/6.txt', 'r') as f:
    input = f.read()

fish = {k: 0 for k in range(9)}
for day in input.split(','):
    fish[int(day)] += 1

print(fish_after_days(fish, 80))
print(fish_after_days(fish, 256))
