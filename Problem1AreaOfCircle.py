#Define a function to compute the area of a circle

import math

def areaofCircle(r):
    area = (r ** 2) * math.pi
    return area

radius = int(input("Enter a radius: "))
print("The area of a circle: ", round(areaofCircle(radius), 2))