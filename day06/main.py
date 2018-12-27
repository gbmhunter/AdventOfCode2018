import os
import pprint

def part1and2():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    coordinates = []
    max_x = 0
    max_y = 0
    with open(os.path.join(script_dir, 'input.txt'), 'r') as file:
        for line in file:
            coordinate_str = line.strip().split(',')
            x = int(coordinate_str[0])
            y = int(coordinate_str[1])
            coordinates.append((x, y))
            max_x = max(max_x, x)
            max_y = max(max_y, y)    
    
    coord_id_to_point = {coord_id: point for coord_id, point in enumerate(coordinates)}    

    # Iterate over each point, finding the closest coordinate
    infinite_coord_ids = set()
    coordinate_areas = {}
    size_of_region_where_distance_less_than_10000 = 0
    for i in range(max_x + 1):
        for j in range(max_y + 1):
            distances = []
            total_distance = 0
            for coord_id, coord_point in coord_id_to_point.items():
                manh_dist = abs(i - coord_point[0]) + abs(j - coord_point[1])                
                distances.append((manh_dist, coord_id))
                total_distance += manh_dist

            if total_distance < 10000:
                size_of_region_where_distance_less_than_10000 += 1

            # This will sort on the first element of the tuple, which is the manhatten distance
            sorted_distances = sorted(distances)            

            if sorted_distances[0][0] != sorted_distances[1][0]:
                coord_id = sorted_distances[0][1]
                # print(f'closest coord has id = {coord_id}, and point = {coord_id_to_point[coord_id]}.')
                try:
                    coordinate_areas[coord_id] += 1
                except KeyError as e:
                    coordinate_areas[coord_id] = 1

                # Any coordinate which has a point on the edge of the boundary
                # is a coordinate with infinite area
                if i == 0 or j == 0 or i == max_x or j == max_y:
                    infinite_coord_ids.add(coord_id)            
        
    sorted_coord_ids = sorted(coordinate_areas, key=coordinate_areas.get, reverse=True)
    for sorted_coord_id in sorted_coord_ids:
        if sorted_coord_id not in infinite_coord_ids:
            break
    
    print(f'part 1: largest area = {coordinate_areas[sorted_coord_id]}')
    print(f'part 2: size of region where locations are less than 10000 away = {size_of_region_where_distance_less_than_10000}')

if __name__ == '__main__':
    part1and2()