

def main():
    with open('input.txt', 'r') as file:
        for line in file:
            input = line

    print(input)

    while(True):

        pre_len = len(input)
        input = find_and_remove_pair(input)
        if pre_len == len(input):
            break

    print(f'Polymer finished reacting. Num. units remaining = {len(input)}')

def find_and_remove_pair(polymer):
    for i in range(len(polymer) - 1):        

        if polymer[i].islower():
            if polymer[i + 1] == polymer[i].upper():
                # print(f'Reaction accuring. Removing {polymer[i]} and {polymer[i + 1]}.')                    
                polymer = polymer[0: i] + polymer[i + 2:]
                return polymer
        elif polymer[i].isupper():
            if polymer[i + 1] == polymer[i].lower():
                # print(f'Reaction accuring. Removing {polymer[i]} and {polymer[i + 1]}.')                    
                polymer = polymer[0: i] + polymer[i + 2:]
                return polymer

    return polymer

main()