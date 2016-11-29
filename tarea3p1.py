#Luis Enrique Jimenez Zavala.
#29/11/2016.
#tarea 3 problema 1.
import numpy as r
import math
lat1=input("introduce la latitud1:")
long1=input("introduce la longitud1:")
lat2=input("introduce la latitud2:")
long2=input("introduce la longitud2:")
def distancia(lat1,long1,lat2,long2):
    x1=lat1*3.1416/180
    x2=long1*3.1416/180
    x3=lat2*3.14146/180
    x4=long2*3.1416/180
    y=6371.01*(math.acos(math.sin(x1))*math.sin(x3)+math.cos(x1)*math.cos(x3)*math.cos(x2-x4))
    return y
print distancia(lat1,long1,lat2,long2)
