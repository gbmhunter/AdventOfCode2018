#!/usr/bin/env python3

from PIL import Image
import numpy as np

class Point:
    def __init__(self, point_str: str):
        print(f'__init__() called with point_str = {point_str}')

        pos_x_start = 10
        pos_x_stop = point_str.find(',', pos_x_start)
        print(pos_x_stop)
        self.x_pos = int(point_str[pos_x_start: pos_x_stop])
        print(f'x_pos = {self.x_pos}')

        pos_y_stop = point_str.find('>', pos_x_stop)
        self.y_pos = int(point_str[pos_x_stop + 1: pos_y_stop])
        print(f'y_pos = {self.y_pos}')

        vel_x_start = point_str.find('<', pos_y_stop) + 1
        vel_x_stop = point_str.find(',', vel_x_start)
        self.x_vel = int(point_str[vel_x_start: vel_x_stop])
        print(f'x_vel = {self.x_vel}')

        vel_y_stop = point_str.find('>', vel_x_stop)
        self.y_vel = int(point_str[vel_x_stop + 1: vel_y_stop])
        print(f'y_vel = {self.y_vel}')

    def __repr__(self):
        return f'x = {self.x_pos}, y = {self.y_pos}\n'

points = []
with open('input.txt', 'r') as file:
    for line in file:
        points.append(Point(line.strip()))

SIZE = 20
OFFSET = 5
# print(point_map)

def draw_point_map(point_map, points):
    # Reset all values back to 0
    point_map.fill(0)
    for point in points:
        print(f'Setting {point.y_pos}, {point.x_pos}')
        point_map[point.y_pos + OFFSET][point.x_pos + OFFSET] = 255

def print_point_map(point_map):
    for row in point_map:
        print(f'{row}\n')

def save_point_map_to_image(point_map, img):
    img.putdata(point_map.flatten())
    img.save('image.png')

# Perform a 1-second step in time, update positions
def perform_1_sec_step(points):
    for point in points:
        point.x_pos += point.x_vel
        point.y_pos += point.y_vel

    # print(f'{str(points)}')

def main():

    # 'L' makes it greyscale
    img = Image.new('L', (SIZE, SIZE))

    # Create point map. DO NOT USE []*SIZE syntax as this
    # does not create unique lists!
    # point_map = []
    # for i in range(SIZE):
    #     point_map.append([])
    #     for j in range(SIZE):
    #         point_map[i].append(' ')
    # point_map[3][3] = '*'
    # print_point_map(point_map)
    # return

    point_map = np.zeros((SIZE, SIZE))
    save_point_map_to_image(point_map, img)    

    for i in range(3):
        perform_1_sec_step(points)
        draw_point_map(point_map, points)
        save_point_map_to_image(point_map, img)

if __name__ == '__main__':
    main()