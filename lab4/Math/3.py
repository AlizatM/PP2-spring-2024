import math

num_sides = int(input())
side_length = int(input())

area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))
print("The area of the polygon is:", int(area))
