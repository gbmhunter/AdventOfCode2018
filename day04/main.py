
def get_minute(line):
    colon_pos = line.find(':') 
    minute_str = line[colon_pos + 1: colon_pos + 3]
    return int(minute_str)

input = []
with open('input.txt', 'r') as file:
    for line in file:
        input.append(line.strip())

input.sort()

guard_sleep_times = {}
total_guard_sleep_time = {}
curr_min = 0
for line in input:
    hash_index = line.find('#')
    if hash_index != -1:
        guard_id = line[hash_index + 1: line.find(' ', hash_index)]

        if not guard_id in guard_sleep_times:
            guard_sleep_times[guard_id] = [0]*60 
            total_guard_sleep_time[guard_id] = 0

        curr_min = 0
    elif line.find('asleep') != -1:
        # Extract minute
        minute = get_minute(line)
        curr_min = minute
            
    elif line.find('wakes') != -1:
        minute = get_minute(line)
        for i in range(curr_min, minute):
            guard_sleep_times[guard_id][i] += 1
            total_guard_sleep_time[guard_id] += 1

        curr_min = minute

# Find guard that slept the longest
def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

key = keywithmaxval(total_guard_sleep_time)
max_value = max(guard_sleep_times[key])
max_index = guard_sleep_times[key].index(max_value)

print(f'Guard {key} slept the most at minute {max_index}. Answer = {int(key)*max_index}')

# PART 2

global_max_guard_id = None
global_max_sleep_min_val = None
global_max_sleep_min = None
for guard_id, sleep_times in guard_sleep_times.items():
    max_sleep_min = max(sleep_times)
    if global_max_guard_id is None:
        global_max_guard_id = guard_id
        global_max_sleep_min_val = max_sleep_min
        global_max_sleep_min = sleep_times.index(max_sleep_min)
    elif max_sleep_min > global_max_sleep_min_val:
        global_max_guard_id = guard_id
        global_max_sleep_min_val = max_sleep_min
        global_max_sleep_min = sleep_times.index(max_sleep_min)

print(f'Guard {global_max_guard_id} slept for the most in minute {global_max_sleep_min} ({global_max_sleep_min_val} times). Answer = {int(global_max_guard_id)*global_max_sleep_min}.')

