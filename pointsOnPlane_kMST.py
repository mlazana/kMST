import itertools
import numpy
import math
import sys

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

# print(len(d))
for pair in d:

    x1 = pair[0][0]
    x2 = pair[1][0]
    y1 = pair[0][1]
    y2 = pair[1][1]

    # print("looking for", pair)
    # Constracting a circle
    circleDiameter = math.sqrt(3)*(d[pair])
    # print("diameter", circleDiameter)
    # Centering the circle at midpont of the line segment
    circleCenter = ((x2+x1)/2,(y2+y1)/2)
    # print(circleCenter)
    # print("___________")

    #Let Sc be the subset of S containedin circle
    Sc = 0
    for point in S:
        # print("this is my pair", pair)
        centerDistance = (point[0]  - circleCenter[0])**2 + (point[1] - circleCenter[1])**2
        # print(centerDistance)
        if centerDistance < circleDiameter/2:
            Sc += 1

    if Sc < k: 
        continue
    else:
        # print(Sc)
        pass
