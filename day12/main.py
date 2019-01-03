def main():
    with open('input_test.txt', 'r') as file:
        initial_state = file.readline()[15:].strip()

        # Next line is empty
        file.readline()

        rules = {}

        for line in file:
            # print(line)
            rules[line[0:5]]  = line[9:10]
    
    print(f'initial_state = {initial_state}')
    print(rules)
    part1(rules, initial_state)

def part1(rules, initial_state):
    print(f'part1() called. rules = {rules}, initial_state = {initial_state}')    

    new_state = '..'
    for i in range(2, len(initial_state) - 2):
        section = initial_state[i - 2 : i + 3]
        print(section)
        if section in rules:
            new_state += '#'
        else:
            new_state += '.'
    new_state += '..'

    # Trim off any trailing '.' (start and end)
    while new_state[0] == '.':
        new_state = new_state[1:]
    
    while new_state[-1] == '.':
        new_state = new_state[:-1]

    print(f'new_state = {new_state}')

if __name__ == '__main__':
    main()