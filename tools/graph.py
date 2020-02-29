import sys
import math

try:
    data_file = sys.argv[1]
except IndexError:
    data_file = 'my.data'

with open(data_file, 'r') as f:
    data = f.read()

pm_points = [pm_point.split(' ') for pm_point in data.split('\n')]
points = [(eval(x), eval(y)) for x, y in pm_points]

x_list = [x for x, y in points]
y_list = [y for x, y in points]

x_max = max(x_list)
x_min = min(x_list)

y_max = max(y_list)
y_min = min(y_list)

x_range = x_max * 1.1, (x_min * 0.9 if x_min > 0 else x_min * (1.1))
y_range = y_max * 1.1, (y_min * 0.9 if y_min > 0 else y_min * (1.1))

del_x = x_range[0] - x_range[1]
del_y = y_range[0] - y_range[1]

no_of_div_x = 160
no_of_div_y = 200

scale_x = del_x / no_of_div_x
scale_y = del_y / no_of_div_y

origin = (x_range[1], y_range[1])
print(f"Origin: {origin}\n\n")

print(f"Scale x: {scale_x}")
print(f"Scale y: { scale_y}\n\n")

print("X axis points:")
for i in range(1, math.ceil(no_of_div_x / 10) + 1):
    print(f"{i * 10} :{round(origin[0] + (i * 10) * scale_x, 2)}")
print('\n')

print("Y axis points:")
for i in range(1, math.ceil(no_of_div_y / 10) + 1):
    print(f"{i * 10} :{round(origin[1] + (i * 10) * scale_y, 2)}")
print('\n')


for point in points:
    x, y = point
    x_ = (x - origin[0]) / scale_x
    y_ = (y - origin[1]) / scale_y
    print(f"Point({point}): ({round(x_)}, {round(y_)})")
