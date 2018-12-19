import os
import pprint

import numpy as np

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'COORD[ x={self.x}, y={self.y} ]'

class ClaimedPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'CLAIMED[ x={self.x}, y={self.y} ]'


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
    # print(grid)

    # Insert coordinates
    for coordinate in coordinates:
        print(f'Adding coordinate {coordinate}.')
        grid[coordinate.x][coordinate.y] = coordinate

    # print(grid)



    # Iterate over each point
    for coordinate in coordinates:
        i = coordinate.x
        j = coordinate.y
        print(f'Finding closest coordinate to ({i}, {j}).')
        points = find_closest_coord(grid, (i, j))
        # pprint.pprint(f'points = {points}')

        closest_coords = []
        furthest_points = points[len(points) - 1] 
        for point_key in furthest_points:
            # print(point_key)
            if isinstance(furthest_points[point_key], Coordinate):
                closest_coords.append(furthest_points[point_key])
        print(f'closest_coords = {closest_coords}')

        distance_to_claim = int((len(points))/2)
        print(f'distance_to_claim = {distance_to_claim}')
        claim_points(grid, points, distance_to_claim, coordinate)
        # if i == 0 and j == 4:
            # pprint.pprint(grid)
            # return

    pprint.pprint(grid) 

        # Iterate over each point
    for i in range(maxX + 1):
        print(f'Finding closest coordinates for x = {i}.')
        for j in range(maxY + 1):
            
            if isinstance(grid[i][j], Coordinate) or isinstance(grid[i][j], ClaimedPoint):
                print(f'Skipping grid[{i}][{j}] as it is = {grid[i][j]}.')
                continue 
            points = find_closest_coord(grid, (i, j))
            # pprint.pprint(f'points = {points}')

            closest_coords = []
            furthest_points = points[len(points) - 1] 
            for point_key in furthest_points:
                # print(point_key)
                if isinstance(furthest_points[point_key], Coordinate):
                    closest_coords.append(furthest_points[point_key])
            # print(f'closest_coords = {closest_coords}')

            if len(closest_coords) == 1:
                # distance_to_claim = int((len(points))/2)
                # print(f'distance_to_claim = {distance_to_claim}')
                # claim_points(grid, points, distance_to_claim, closest_coords[0])
                grid[i][j] = ClaimedPoint(closest_coords[0].x, closest_coords[0].y)
            else:
                # print('Two coordinates are equally the closest, cannot assign.')
                pass
            # if i == 0 and j == 4:
                # pprint.pprint(grid)
                # return


    # print('FINISHED. grid =')
    # pprint.pprint(grid)
    max_area = count_largest_area(grid)
    print(f'max_area = {max_area}')

def count_largest_area(grid):
    areas = {}
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            point = grid[x][y]
            if point is None:
                continue
            key = (point.x, point.y)
            if x == 0 or x == len(grid) - 1 or y == 0 or y == len(grid[0]) - 1:
                areas[key] = None
                continue

            if key in areas:
                if areas[key] is None:
                    continue
                areas[key] += 1
                continue
            else:
                areas[key] = 1
    # pprint.pprint(areas)

    max_area = 0
    for area_key in areas:
        if areas[area_key] is None:
            continue
        if areas[area_key] > max_area:
            max_area = areas[area_key]

    return max_area

def claim_points(grid, points, distance, closest_coord):
    print(f'claim_points() called with distance = {distance}, num_points = {len(points)}.')

    for i in range(distance):
        points_at_distance_i = points[i]
        # print(f'points_at_distance_i = {points_at_distance_i}')
        for point in points_at_distance_i:
            if grid[point[0]][point[1]] == None:
                # print(f'Claiming ({point[0]},{point[1]}) for ({closest_coord.x}, {closest_coord.y}).')
                grid[point[0]][point[1]] = ClaimedPoint(closest_coord.x, closest_coord.y)

def find_closest_coord(grid, point_loc):
    """

    Returns:
        Returns list. Each list index contains an array of points where the index is also equal to
        the manhatten distance from point_loc.
    """
    # print(f'Finding closest coord for location {point_loc[0]}, {point_loc[1]}.')

    manhatten_dist = 1
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
            # print(f'Found coordinate at distance = {manhatten_dist}')
            return points
        # print(points)

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
                if x >= len(grid) or x < 0 or y >= len(grid[0]) or y < 0:
                    # print('Grid index out-of-bounds.')
                    points_at_manhatten_dist[(x, y)] = 'oob'
                else:
                    # print(f'x = {x}, y = {y}, grid[x,y] = {grid[x][y]}')
                    points_at_manhatten_dist[(x, y)] = grid[x][y]

    # print(points_at_manhatten_dist)
    return points_at_manhatten_dist


if __name__ == '__main__':
    main()