import re

def sum_points():
    with open('./day4.txt') as file:
        total_points = 0
        for line in file.readlines():
            point_value = 0
            win_nums = re.findall(r'(\d+)', line[10:39])
            sample_nums = re.findall(r'(\d+)',line[42:len(line)-1])
            for num in sample_nums:
                if num in win_nums:
                    point_value = 1 if point_value == 0 else 2*point_value
            total_points += point_value
        return total_points

answer = sum_points()



