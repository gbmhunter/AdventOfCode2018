input = []
with open('input.txt', 'r') as file:
    for line in file:
        input.append(line.strip())

input.sort()
print(input)

guard_sleep_times = {}
curr_min = 0
for line in input:
    print(line)

    # date = line[1:11]
    # print(date)

    hash_index = line.find('#')
    if hash_index != -1:
        print('New guard')
        guard_id = line[hash_index + 1: line.find(' ', hash_index)]
        print(guard_id)

        if not guard_id in guard_sleep_times:
            guard_sleep_times[guard_id] = [0]*60 

        curr_min = 0

print(guard_sleep_times)