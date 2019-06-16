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
    # Creating distances based on euclidean distance for every pair
    d[pair] = math.sqrt(((pair[0][0]-pair[1][0])**2)+((pair[0][1]-pair[1][1])**2))

for pair in d:
    print(pair)
    # Constracting a circle
    circleDiameter = math.sqrt(3)*(d[pair])
    # Centering the circle at midpont of the line segment
    cicleCenter = ((pair[0][0]-pair[1][0])/2,(pair[0][1]-pair[1][1])/2)
    #print("%.2f" % circleDiameter)
    #print(cicleCenter)

    #Let Sc be the subset of S containedin circle
    Sc = 0
    for p in S:
        centerDistance = (p[0] - cicleCenter[0])**2 + (p[1] - cicleCenter[1])**2
        if centerDistance < circleDiameter/2:
            Sc += 1

    if Sc < k: 
        continue
    else:
        print(Sc)
