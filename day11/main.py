import numpy as np
np.set_printoptions(threshold=np.nan)

GRID_SERIAL_NUMBER = 6042
GRID_SIZE = 300

def main():

    # PART 1
    grid = np.zeros((GRID_SIZE, GRID_SIZE))
    calc_cell_power(grid)

    cell_powers = {}
    for y in range(GRID_SIZE - 2):
        for x in range(GRID_SIZE - 2):
            cell_power = calc_group_power(grid, x, y)        
            cell_powers[(y,x)] = cell_power

    # Find max. power
    max_power_key = max(cell_powers, key=cell_powers.get)    
    max_power_value = cell_powers[max_power_key]    
    max_power_coordinate = (max_power_key[1] + 1, max_power_key[0] + 1)
    print(f'max. power at coordinate {max_power_coordinate}, power = {max_power_value}.')

    # PART 2
    cell_powers_2 = {}
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            calc_powers_for_all_sizes_starting_at_cell(grid, x, y, cell_powers_2)   

    # Find max. power
    max_power_key = max(cell_powers_2, key=cell_powers_2.get)    
    max_power_value = cell_powers_2[max_power_key]    
    max_power_coordinate = (max_power_key[1] + 1, max_power_key[0] + 1, max_power_key[2])
    print(f'max. power at coordinate {max_power_coordinate}, power = {max_power_value}.')
                     

def calc_cell_power(grid):
    for y in range(GRID_SIZE):
        y_coord = y + 1
        for x in range(GRID_SIZE):
            x_coord = x + 1
            rack_id = x_coord + 10
            power_level = rack_id * y_coord
            power_level += GRID_SERIAL_NUMBER
            power_level *= rack_id
            try:
                power_level = int((str(power_level))[-3])
            except IndexError as e:
                power_level = 0
            power_level -= 5
            grid[y,x] = power_level

def calc_group_power(grid, x, y):
    # Sum 3x3 to calculate power
    cell_power = 0
    for i in range(3):
        for j in range(3):
            cell_power += grid[y + i, x+ j]
    return cell_power

def calc_powers_for_all_sizes_starting_at_cell(grid, x, y, powers_dict):
    # Calculate max. square that can be made at this x,y location
    max_grid_size = min(GRID_SIZE - x, GRID_SIZE - y)

    cell_power = 0
    for grid_size in range(1, max_grid_size + 1):
        for i in range(grid_size):
            cell_power += grid[y + grid_size - 1, x + i]

        for j in range(grid_size - 1):
            cell_power += grid[y + j, x + grid_size - 1]

        powers_dict[(y,x,grid_size)] = cell_power

if __name__ == '__main__':
    main()

