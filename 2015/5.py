exclusions = ['ab', 'cd', 'pq', 'xy']
vowels = 'aeiou'


def rule_1(string):
    count = 0
    for c in string:
        if c in vowels:
            count += 1
    return count > 2


def rule_2(string):
    for idx in range(1, len(string)):
        x = string[idx-1]
        y = string[idx]
        if x == y:
            return True
    return False


def rule_3(string):
    for exclusion in exclusions:
        if exclusion in string:
            return True
    return False


def rule_4(string):
    for idx in range(0, len(string)-2):
        s = ''.join(string[idx:idx+2])
        if s in string[idx+2:]:
            return True
    return False


def rule_5(string):
    for idx in range(0, len(string)-2):
        if string[idx] == string[idx+2]:
            return True
    return False


def day5_ex1(word):
    # print(f'{word}: {rule_1(word)}, {rule_2(word)}, {rule_3(word)}')
    return not rule_3(word) and rule_1(word) and rule_2(word)


def day5_ex2(word):
    # print(f'{word}: {rule_4(word)}, {rule_5(word)}')
    return rule_4(word) and rule_5(word)


with open('files/4.txt', 'r') as f:
    words = [word for word in map(lambda x: x.rstrip('\n'), f.readlines())]

print('Check for ex1')
print('-------------')
print(day5_ex1('ugknbfddgicrmopn'))
print(day5_ex1('aaa'))
print(day5_ex1('jchzalrnumimnmhp'))
print(day5_ex1('haegwjzuvuyypxyu'))
print(day5_ex1('dvszwmarrgswjxmb'), '\n')

print('Result of ex1')
print('-------------')
print(sum(map(lambda word: day5_ex1(word), words)), '\n')

print('Check for ex2')
print('-------------')
print(day5_ex2('qjhvhtzxzqqjkmpb'))
print(day5_ex2('xxyxx'))
print(day5_ex2('uurcxstgmygtbstg'))
print(day5_ex2('ieodomkazucvgmuy'), '\n')

print('Result of ex2')
print('-------------')
print(sum(map(lambda word: day5_ex2(word), words)))
