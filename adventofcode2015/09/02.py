from collections import defaultdict
from itertools import permutations


with open('input') as f:
    routes = f.read().splitlines()

# This is exactly the Traveling Salesman problem, no?

cities = set()
trips = defaultdict(dict)

for route in routes:
    trip, dist = route.split(' = ')
    start, end = trip.split(' to ')
    cities.add(start)
    cities.add(end)
    trips[start][end] = int(dist)
    trips[end][start] = int(dist)

round_trips = permutations(cities)

best_trip_dist = -99

for rt in round_trips:
    this_trip_dist = 0
    for i in range(len(rt)-1):
        this_trip_dist += trips[rt[i]][rt[i+1]]
    if this_trip_dist > best_trip_dist:
        best_trip_dist = this_trip_dist

print(best_trip_dist)
