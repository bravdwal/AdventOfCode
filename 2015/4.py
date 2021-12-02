import hashlib

input = 'yzbqklnj'


def is_solution(hash):
    return hash.startswith('000000')


num = 0
while not is_solution(hashlib.md5(f'{input}{num}'.encode()).hexdigest()):
    num += 1

print(num)
