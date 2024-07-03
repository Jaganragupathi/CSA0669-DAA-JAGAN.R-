def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1  
    else:
        return 2  
def convex_hull(points):
    n = len(points)
    if n < 3:
        return points
    points = sorted(points)
    hull = []
    for p in points:
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], p) != 2:
            hull.pop()
        hull.append(p)
    for p in reversed(points[:-1]):
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], p) != 2:
            hull.pop()
        hull.append(p)
    hull = list(dict.fromkeys(hull))
    return hull
points = [(1, 1), (4, 6), (8, 1), (0, 0), (3, 3)]
convex_hull_points = convex_hull(points)
print("Convex hull points:", convex_hull_points)
