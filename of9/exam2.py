import math


def edge_length(x1, y1, x2, y2):
    return math.sqrt( (x1 - x2) ** 2 + (y1 - y2) ** 2)


def circumference(p_list):
    if len(p_list) == 0 or len(p_list) % 2 == 1:
        return -1

    if len(p_list) == 2:
        return 0

    circum = 0
    for i in range(0, len(p_list) - 3, 2):
        circum += edge_length(p_list[i], p_list[i + 1], p_list[i + 2], p_list[i + 3])
    circum += edge_length(p_list[-2], p_list[-1], p_list[0], p_list[1])
    return circum


def enclosing_rectangle(p_list):
    x_vars = p_list[::2]
    y_vars = p_list[1::2]

    min_x = min(x_vars)
    max_x = max(x_vars)
    min_y = min(y_vars)
    max_y = max(y_vars)

    return [min_x, min_y, max_x, max_y]


def enclosing_rectangle2(p_list):
    min_x = p_list[0]
    max_x = p_list[0]
    min_y = p_list[1]
    max_y = p_list[1]

    for i in range(2, len(p_list)):
        if i % 2 == 1:
            # X-vars
            if p_list[i] > max_x:
                max_x = p_list[i]
            if p_list[i] < min_x:
                min_x = p_list[i]
        else:
            # Y-vars
            if p_list[i] > max_y:
                max_y = p_list[i]
            if p_list[i] < min_y:
                min_y = p_list[i]

    return [min_x, min_y, max_x, max_y]


def read_polygon_file(filename):
    coords = []

    with open(filename, 'r') as f:
        for line in f:
            info = line.split()
            coords.append(int(info[0]))
            coords.append(int(info[1]))
    return coords

polygon = read_polygon_file('coords.txt')
print(polygon)
print("Circumference:", circumference(polygon))
print("Rect:", enclosing_rectangle(polygon))