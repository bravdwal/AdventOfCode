import re
import itertools


def get_cost(graph, permutation):
    cost = 0
    for idx in range(1, len(permutation)):
        frm = permutation[idx-1]
        to = permutation[idx]
        cost += graph[frm][to]
    return cost


with open('files/9.txt', 'r') as f:
    lines = f.readlines()

graph = dict()
cities = set()

for line in lines:
    m = re.search(r'^(\w+) to (\w+) = (\d+)$', line)
    frm, to, cost = m.groups()
    cost = int(cost)

    # just blindly add, its a set...
    cities.add(frm)
    cities.add(to)

    if frm not in graph:
        graph[frm] = {to: cost}
    else:
        graph[frm][to] = cost

    if to not in graph:
        graph[to] = {frm: cost}
    else:
        graph[to][frm] = cost

permutations = list(itertools.permutations(cities))

current_min = get_cost(graph, permutations[0])
current_min_perm = permutations[0]

current_max = current_min
current_max_perm = current_min_perm

for perm in permutations[1:]:
    if (cost := get_cost(graph, perm)) < current_min:
        current_min = cost
        current_min_perm = perm
    elif cost > current_max:
        current_max = cost
        current_max_perm = perm

print(current_min_perm)
print(current_min, '\n')
print(current_max_perm)
print(current_max)
