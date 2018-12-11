#!/usr/bin/env python3

from PIL import Image
import numpy as np

IMAGE_SIZE = 300
IMAGE_OFFSET = 0

class Point:
    def __init__(self, point_str: str):
        pos_x_start = 10
        pos_x_stop = point_str.find(',', pos_x_start)
        self.x_pos = int(point_str[pos_x_start: pos_x_stop])

        pos_y_stop = point_str.find('>', pos_x_stop)
        self.y_pos = int(point_str[pos_x_stop + 1: pos_y_stop])

        vel_x_start = point_str.find('<', pos_y_stop) + 1
        vel_x_stop = point_str.find(',', vel_x_start)
        self.x_vel = int(point_str[vel_x_start: vel_x_stop])

        vel_y_stop = point_str.find('>', vel_x_stop)
        self.y_vel = int(point_str[vel_x_stop + 1: vel_y_stop])

def main():
    points = {}
    with open('input.txt', 'r') as file:
        for line in file:
            point = Point(line.strip())
            key = (point.x_pos, point.y_pos)
            if not key in points:
                points[key] = []
            points[key].append(point)

    # 'L' makes it greyscale
    img = Image.new('L', (IMAGE_SIZE, IMAGE_SIZE))
    point_map = np.zeros((IMAGE_SIZE, IMAGE_SIZE)) 

    num_iterations = 0
    while(True):
        connectivity = calc_connectivity(points)
        if connectivity > 600:
            print(f'connectivity = {connectivity}, num. seconds = {num_iterations}')
            draw_and_save_point_map(points, point_map, img)
            break
        points = perform_1_sec_step(points)
        num_iterations += 1

def draw_and_save_point_map(points, point_map, img):
    # Reset all values back to 0
    point_map.fill(0)
    for key in points:
        for point in points[key]:
            point_map[point.y_pos + IMAGE_OFFSET][point.x_pos + IMAGE_OFFSET] = 255

    img.putdata(point_map.flatten())
    img.save('image.png')

# Perform a 1-second step in time, update positions
def perform_1_sec_step(points):
    new_points = {}
    for key in points:
        points_list = points[key]
        for point in points_list:
            point.x_pos += point.x_vel
            point.y_pos += point.y_vel
            new_key = (point.x_pos, point.y_pos)
            if not new_key in new_points:
                new_points[new_key] = []
            new_points[new_key].append(point)        
    return new_points

def calc_connectivity(points):    
    connectivity = 0
    for key in points:
        points_list = points[key]
        for point in points_list:
            if (point.x_pos - 1, point.y_pos) in points:
                connectivity += 1
            if (point.x_pos + 1, point.y_pos) in points:
                connectivity += 1
            if (point.x_pos, point.y_pos - 1) in points:
                connectivity += 1
            if (point.x_pos, point.y_pos + 1) in points:
                connectivity += 1
    return connectivity

if __name__ == '__main__':
    main()