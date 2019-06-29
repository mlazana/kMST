import itertools
import numpy
import math
from math import atan2,degrees
import sys


'''
This functions returns the four points of a square
in a plane (k1,k2,k3,k4)

k1--------k2
|          |
|          |
|          |
k4--------k3
'''

def getSquarePoints(x1,x2,y1,y2,radius):

    # Angle of line
    angle = math.degrees(atan2(y2-y1,x2-x1))
    
    k1_x = round(radius*(math.cos(math.radians(angle+90))) + x1,2)
    k1_y = round(radius*(math.sin(math.radians(angle+90))) + y1,2)

    k2_x = round(radius*(math.cos(math.radians(angle+90))) + x2,2)
    k2_y = round(radius*(math.sin(math.radians(angle+90))) + y2,2)

    k3_x = round(radius*(math.cos(math.radians(angle-90))) + x1,2)
    k3_y = round(radius*(math.sin(math.radians(angle-90))) + y1,2)

    k4_x = round(radius*(math.cos(math.radians(angle-90))) + x2,2)
    k4_y = round(radius*(math.sin(math.radians(angle+90))) + y2,2)

    squarePoints = [k1_x,k1_y,k2_x,k2_y,k3_x,k3_y,k4_x,k4_y]

    return squarePoints

S = []
d = {}

#k is given as an input
k = 2

#read each line from the file
with open(sys.argv[1]) as f:
    for line in f:
        c = [x.strip() for x in line.split(',')]
        #list S containes tuples of x,y coordinates
        S.append((int(c[0]),int(c[1])))


    
# For any pair of points si and sj, 
# let d(i,j) denote the Euclidean distance between si and sj.
for pair in itertools.combinations(S,2):

    x1 = pair[0][0]
    x2 = pair[1][0]
    y1 = pair[0][1]
    y2 = pair[1][1]
    # Creating distances based on euclidean distance for every pair
    d[pair] = math.sqrt(((x1 - x2)**2)+((y1-y2)**2))

    # Constracting a circle
    circleDiameter = math.sqrt(3)*(d[pair])
    # Centering the circle at midpont of the line segment
    circleCenter = ((x2+x1)/2,(y2+y1)/2)

    #Let Sc be the subset of S containedin circle
    Sc = {}
    values = []
    for point in S:
        # print("this is my pair", pair)
        centerDistance = (point[0]  - circleCenter[0])**2 + (point[1] - circleCenter[1])**2
        # print(centerDistance)
        if centerDistance < circleDiameter/2:
            key = pair
            Sc.setdefault(key, [])
            Sc[key].append(point)