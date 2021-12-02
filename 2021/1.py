import re

with open('files/1.txt', 'r') as f:
    measurements = f.readlines()


depths = []
for measurement in measurements:
    m = re.search(r'(\d+)', measurement)
    depth, = m.groups()
    depths.append(int(depth))

count = 0
for i in range(1, len(depths)):
    if depths[i-1] < depths[i]:
        count += 1

print(count)

grouped_depths = []
for i in range(2, len(depths)):
    grouped_depths.append(depths[i-2] + depths[i-1] + depths[i])

count = 0
for i in range(1, len(grouped_depths)):
    if grouped_depths[i-1] < grouped_depths[i]:
        count += 1

print(count)
