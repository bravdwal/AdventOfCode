with open('files/3.txt', 'r') as f:
    lines = list(map(lambda line: line[:-1] if line[-1] == '\n' else line, f.readlines()))

N_LINES = len(lines)


def get_freq_zero(lines):
    freq_zero = [0 for _ in range(len(lines[0]))]
    for line in lines:
        for idx, c in enumerate(line):
            if c == '0':
                freq_zero[idx] += 1
    return freq_zero


# gamma rate & epsilon_rate
freq_zero = get_freq_zero(lines)
gamma_rate = int(''.join(['0' if freq > N_LINES/2 else '1' for freq in freq_zero]), 2)
epsilon_rate = int(''.join(['1' if freq > N_LINES/2 else '0' for freq in freq_zero]), 2)
print(gamma_rate*epsilon_rate)


# oxygen generating rating
filtered = lines
idx = 0
while len(filtered) > 1:
    freq_zero = get_freq_zero(filtered)
    n_lines = len(filtered)
    filtered = list(filter(lambda line: line[idx] == ('0' if freq_zero[idx] > n_lines/2 else '1'), filtered))
    idx += 1

oxygen_generating_rating = int(filtered[0], 2)

# CO2 scrubber rating
filtered = lines
idx = 0
while len(filtered) > 1:
    freq_zero = get_freq_zero(filtered)
    n_lines = len(filtered)
    filtered = list(filter(lambda line: line[idx] == ('1' if freq_zero[idx] > n_lines/2 else '0'), filtered))
    idx += 1

co2_scrubber_rating = int(filtered[0], 2)

print(oxygen_generating_rating*co2_scrubber_rating)
