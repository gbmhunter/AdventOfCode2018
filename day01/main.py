# PART 1
sum = 0
with open('input.txt', 'r') as file:
    for line in file:
        sum += int(line)

print(f'sum = {sum}')

# PART 2
freq = 0
set_of_freqs = set()
with open('input.txt', 'r') as file:
    lines = file.readlines()

found_repeated = False
while(not found_repeated):
    for line in lines:
        freq_change = int(line)
        freq += freq_change
        if freq in set_of_freqs:
            print(f'Found first repeated frequency of {freq}.')
            found_repeated = True
            break
        else:
            set_of_freqs.add(freq)
        
