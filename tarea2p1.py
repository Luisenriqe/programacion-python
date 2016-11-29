import math
cat1 = input ("ingrese el cateto 1:")
cat2 = input ("ingrese el cateto 2:")
def hip():
    return math.sqrt(cat1*2 + cat2*2)
print "hipotesa es:",hip
