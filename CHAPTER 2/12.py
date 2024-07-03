def distance(city1, city2):
    return ((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)**0.5

def tsp(cities):
    n = len(cities)
    shortest_path = None
    min_distance = float('inf')
    def generate_permutations(cities):
        if len(cities) <= 1:
            return [cities]
        permutations = []
        for i, city in enumerate(cities):
            rest = cities[:i] + cities[i+1:]
            for perm in generate_permutations(rest):
                permutations.append([city] + perm)
        return permutations
    for perm in generate_permutations(cities[1:]):
        path = [cities[0]] + list(perm) + [cities[0]]
        total_distance = sum(distance(path[i], path[i+1]) for i in range(n))
        if total_distance < min_distance:
            min_distance = total_distance
            shortest_path = path
    return min_distance, shortest_path
cities1 = [(1, 2), (4, 5), (7, 1), (3, 6)]
cities2 = [(2, 4), (8, 1), (1, 7), (6, 3), (5, 9)]
min_distance1, shortest_path1 = tsp(cities1)
min_distance2, shortest_path2 = tsp(cities2)
print("Test Case 1:")
print(f"Shortest Distance: {min_distance1}")
print(f"Shortest Path: {shortest_path1}\n")
print("Test Case 2:")
print(f"Shortest Distance: {min_distance2}")
print(f"Shortest Path: {shortest_path2}")
