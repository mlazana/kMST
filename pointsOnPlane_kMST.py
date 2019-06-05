import itertools
import numpy
import math

S = [1,2,3,4]
d = {}

# For any pair of points si and sj, 
# let d(i,j) denote the Euclidean distance between si and sj.
for pair in itertools.product(S, repeat=2):
    if pair[0] != pair[1]:
        # Creating distances based on euclidean distance
        d[pair] = numpy.linalg.norm(abs(pair[0]-pair[1]))

for pair in d:
    print(pair)
    # Constracting a circle
    circleDiameter = math.sqrt(3)*(d[pair])
    # Centering the circle at midpont of the line segment
    cicleCenter = ((pair[0] + pair[1])/ 2)

  


