import string


def main():
    with open('input.txt', 'r') as file:
        for line in file:
            input = line

    # Create a list which remember which polymers in the input have reacted
    reacted_list = [False]*len(input)
    remaining_length = react_polymer(input, reacted_list)
    print(f'part 1: remaining length = {remaining_length}')

    list_of_letters = list(string.ascii_lowercase)

    polymer_lengths = {}
    for letter in list_of_letters:
        reacted_list = [False]*len(input)
        remove_unit_type(input, reacted_list, letter)
        remaining_length = react_polymer(input, reacted_list)
        polymer_lengths[letter] = remaining_length

    min_polymer_key = min(polymer_lengths, key=polymer_lengths.get)
    print(f'part 2: smallest polymer = {polymer_lengths[min_polymer_key]}')

def react_polymer(polymer, reacted_list):
    find_pairs(polymer, reacted_list)

    num_unreacted_units = 0
    for unit in reacted_list:
        if unit == False:
            num_unreacted_units += 1
    return num_unreacted_units

def find_pairs(polymer, reacted_list):
    at_least_one_reaction_occurred = True
    loop_count = 0
    length_polymer = len(polymer)
    while(at_least_one_reaction_occurred):
        at_least_one_reaction_occurred = False
        i = 0

        while(i < length_polymer - 1):
            # Get next unreacted unit
            first_index = get_next_unreacted_unit(reacted_list, i)
            if first_index is None:
                break

            second_index = get_next_unreacted_unit(reacted_list, first_index + 1)
            if second_index is None:
                break

            if polymer[first_index].islower():
                if polymer[second_index] == polymer[first_index].upper():
                    reacted_list[first_index] = True
                    reacted_list[second_index] = True
                    at_least_one_reaction_occurred = True
                    i = max(0, first_index - 1)
                    continue
            elif polymer[first_index].isupper():
                if polymer[second_index] == polymer[first_index].lower():
                    reacted_list[first_index] = True
                    reacted_list[second_index] = True
                    at_least_one_reaction_occurred = True
                    i = max(0, first_index - 1)
                    continue
            
            i = second_index
            
def get_next_unreacted_unit(reacted_list, start_index):
    for i in range(start_index, len(reacted_list)):
        if reacted_list[i] == False:
            return i

    return None

def remove_unit_type(polymer, reacted_list, unit_type):
    for i in range(len(polymer)):
        if polymer[i].lower() == unit_type:
            reacted_list[i] = True

if __name__ == '__main__':
    main()