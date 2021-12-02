import numpy as np


def wrapping_area(dim):
    return 3*dim[0]*dim[1] + 2*dim[0]*dim[2] + 2*dim[1]*dim[2]


def ribbon_area(dim):
    return 2*dim[0] + 2*dim[1] + np.prod(dim)


# check utils
print(wrapping_area([2, 3, 4]))
print(wrapping_area([1, 1, 10]))
print(ribbon_area([2, 3, 4]))
print(ribbon_area([1, 1, 10]))

with open('files/2.txt', 'r') as f:
    dimensions = f.readlines()

dimensions = [sorted([int(c) for c in line[:-1].split('x')]) for line in dimensions]
wrapping_areas = [wrapping_area(dim) for dim in dimensions]
ribbon_areas = [ribbon_area(dim) for dim in dimensions]

print(sum(wrapping_areas))
print(sum(ribbon_areas))
