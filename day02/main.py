
# PART 1
box_ids = []
with open('input.txt', 'r') as file:
    for line in file:
        box_ids.append(line.strip())

letters_2 = 0
letters_3 = 0
for box_id in box_ids:
    letters_and_freq = {}
    for char in box_id:
        if char in letters_and_freq:
            letters_and_freq[char] += 1
        else:
            letters_and_freq[char] = 1
    
    for char in letters_and_freq:
        if letters_and_freq[char] == 2:
            letters_2 += 1
            break

    for char in letters_and_freq:
        if letters_and_freq[char] == 3:
            letters_3 += 1
            break

checksum = letters_2*letters_3
print(f'checksum = {checksum}')

# PART 2
found_match = False
for i in range(len(box_ids)):
    for j in range(i + 1, len(box_ids)):
        id1 = box_ids[i]
        id2 = box_ids[j]
        
        num_of_diff_chars = 0
        for k in range(len(id1)):            
            if id1[k] != id2[k]:
                num_of_diff_chars += 1

        if num_of_diff_chars == 1:
            found_match = True

        if found_match:
            break

    if found_match:
        break

shared_chars = ''
for k in range(len(id1)):
    if id1[k] == id2[k]:
        shared_chars += id1[k]

print(f'shared_chars = {shared_chars}')
