import math
points = [(1, 2), (4, 5), (7, 8), (3, 1)]  
min_dist= float('inf')
closest_pair = None
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = math.sqrt((points[j][0] - points[i][0])**2 + (points[j][1] - points[i][1])**2)
        if dist < min_dist:
            min_dist = dist
            closest_pair = (points[i], points[j])
print("Closest pair: {closest_pair}")
print(f"Minimum distance: {min_dist}")
