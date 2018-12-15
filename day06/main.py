import os

import numpy as np

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'C[ x={self.x}, y={self.y} ]'

class ClaimedPoint:
    pass

coordinates = []
def main():
    
    script_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_dir, 'input.txt'), 'r') as file:
        for line in file:
            coordinate_str = line.strip().split(',')
            coordinate = Coordinate(int(coordinate_str[0]), int(coordinate_str[1]))
            coordinates.append(coordinate)
    print(coordinates)

    # Find min/max coordinates to define grid
    minX = coordinates[0].x
    maxX = coordinates[0].x
    minY = coordinates[0].y
    maxY = coordinates[0].y
    for coordinate in coordinates:
        if coordinate.x < minX:
            minX = coordinate.x
        if coordinate.x > maxX:
            maxX = coordinate.x
        if coordinate.y < minY:
            minY = coordinate.y
        if coordinate.y > maxY:
            maxY = coordinate.y
    
    print(f'minX = {minX}, maxX = {maxX}, minY = {minY}, maxY = {maxY}')
    # Create grid
    # grid = np.zeros((maxX - minX, maxY - minY))
    grid = []
    for i in range(maxX + 1):
        grid.append([])
        for j in range(maxY + 1):
            grid[i].append(None)
    print(grid)

    # Insert coordinates
    for coordinate in coordinates:
        print(f'Adding coordinate {coordinate}.')
        grid[coordinate.x][coordinate.y] = coordinate

    print(grid)

    # Iterate over each point
    for i in range(maxX + 1):
        for j in range(maxY + 1):
            points = find_closest_coord(grid, (i, j))
            print(f'points = {points}')
            distance_to_claim = int((len(points)+1)/2)
            print(f'distance_to_claim = {distance_to_claim}')


def find_closest_coord(grid, point_loc):
    print(f'Finding closest coord for location {point_loc[0]}, {point_loc[1]}.')

    manhatten_dist = 0
    points = []
    while(True):
        # Search around point location
        found_points = search_manhatten(grid, point_loc, manhatten_dist)
        points.append(found_points)

        init_length = len(found_points)
        out_of_bounds = 0
        found_at_least_one_coord = False
        for key in list(found_points.keys()):
            if isinstance(found_points[key], Coordinate):
                # print('Found coordinate.')
                found_at_least_one_coord = True
            elif found_points[key] == 'oob':
                found_points.pop(key)
                out_of_bounds += 1
            else:
                # print('Found normal point.')
                pass
                

        if out_of_bounds == init_length:
            # print(f'All points where out-of-bounds.')
            return None
        
        if found_at_least_one_coord:
            return points
        print(points)

        # No coordinates found at this manhatten distance, increase distance by one
        # and try again (we are still within the bounds of the grid)
        manhatten_dist += 1

def search_manhatten(grid, point_loc, manhatten_dist):
    points_at_manhatten_dist = {}
    for delta_x in range(manhatten_dist + 1):
        delta_y = manhatten_dist - delta_x

        # Generate four points,
        # (+x,+y), (-x,+y), (+x,-y), (-x,-y)
        for sign_x in [-1, 1]:
            for sign_y in [-1, 1]:
                x = point_loc[0] + sign_x*delta_x
                y = point_loc[1] + sign_y*delta_y
                if x >= len(grid) or y >= len(grid[0]):
                    # print('Grid index out-of-bounds.')
                    points_at_manhatten_dist[(x, y)] = 'oob'
                else:
                    # print(f'x = {x}, y = {y}, grid[x,y] = {grid[x][y]}')
                    points_at_manhatten_dist[(x, y)] = grid[x][y]

    # print(points_at_manhatten_dist)
    return points_at_manhatten_dist


if __name__ == '__main__':
    main()