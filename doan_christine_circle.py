# Programmer: Christine Doan
# Assignment 4, Functions

# Part 3: Spherical Distance
# Calculate distances between cities

# import

from math import radians, degrees, sin, cos, asin, acos, sqrt

# latitudes and longitudes

# san jose
sjlat = 37.33
sjlong = -121.9

# chicago
chilat = 41.83
chilong = -87.68

# washington
washlat = 38.90
washlong = -77.02

# functions
def great_circle_distance (lat1, long1, lat2, long2):
    lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])
    return 6371 * (acos (sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos((abs(long1 - long2)))))

def km_to_miles (km):
    ratio = 0.621371
    return km * ratio

# calculations
sj_chikm = great_circle_distance(sjlat, sjlong, chilat, chilong)
sj_chimi = km_to_miles (sj_chikm)

chi_washkm = great_circle_distance(chilat, chilong, washlat, washlong)
chi_washmi =  km_to_miles (chi_washkm)

# outputs
print("Distance from San Jose to Chicago is", (int(sj_chikm)), "km or", (int(sj_chimi)), "miles.")
print("Distance from Chicago to Washington DC is", (int(chi_washkm)), "km or", (int(chi_washmi)), "miles.")