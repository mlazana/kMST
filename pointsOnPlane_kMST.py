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
   
    k3_x = round(radius*(math.cos(math.radians(angle-90))) + x2,2)
    k3_y = round(radius*(math.sin(math.radians(angle-90))) + y2,2)
   
    k4_x = round(radius*(math.cos(math.radians(angle-90))) + x1,2)
    k4_y = round(radius*(math.sin(math.radians(angle-90))) + y1,2)

    squarePoints = [k1_x,k1_y,k2_x,k2_y,k3_x,k3_y,k4_x,k4_y]

    return squarePoints

S = []
d = {}

#k is given as an input
k = 1

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
    circleDiameter = round(math.sqrt(3)*(d[pair]),2)
    print("circleDiameter:",circleDiameter)
    # New edge points 
    if x1 < x2:
        x1 = round(pair[0][0] - circleDiameter/2,2)
        x2 = round(pair[1][0] + circleDiameter/2,2)
    else:
        x1 = round(pair[0][0] + circleDiameter/2,2)
        x2 = round(pair[1][0] - circleDiameter/2,2)
    print("New x1:",x1,"New x2",x2)
    # Centering the circle at midpont of the line segment
    circleCenter = (round((x2+x1)/2,2),round((y2+y1)/2),2)

    #Let Sc be the subset of S containedin circle
    Sc = {}
    values = []
    #print("this is my pair", pair)
    for point in S:
        #print("point:", point)
        #print("Circle center:", circleCenter)
        centerDistance = round(math.sqrt((point[0]  - circleCenter[0])**2 + (point[1] - circleCenter[1])**2),2)
        #print("centerDistance: ",centerDistance)
        if centerDistance <= circleDiameter/2:
            key = pair
            Sc.setdefault(key, [])
            Sc[key].append(point)

    #print("Sc:",Sc)
    print("Pair",pair)
    if  len(Sc[pair]) > k  :
        # Let Q be the square of side 5 circumscribing C.
        # Returns a list of [k1_x,k1_y,k2_x,k2_y,k3_x,k3_y,k4_x,k4_y] points
        Q = getSquarePoints(x1,x2,y1,y2,circleDiameter/2)

        print("SquarePoints :  ",Q)
        print("---------------")

        # Divide Q into k square cells each with side circleDiameter/sqrt(k)
        #mporei na vvgalei error outof range
        side = circleDiameter/round(math.sqrt(k),2)
        subSquares = {}
        k_x = Q[0]
        k_y = Q[1]
        for i in range(k):
            x1 = k_x
            y1 = k_y - side/2
            x2 = k_x + side
            y2 = y1
            
            subSquares[i]= getSquarePoints(x1,x2,y1,y2,side)
            #print("SubSquares",subSquares)
            
            if k_x + side < Q[2]:
                k_x += side
            else:
                k_x = Q[0]
                k_y = k_y - side  
    else:
        continue
    


