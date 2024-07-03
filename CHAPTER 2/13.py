import itertools
def total_cost(assignment, cost_matrix):
    total = 0
    for worker, task in enumerate(assignment):
        total += cost_matrix[worker][task]
    return total
def assignment_problem(cost_matrix):
    num_workers = len(cost_matrix)
    tasks = range(num_workers)
    
    min_cost = float('inf')
    optimal_assignment = None   
    for perm in itertools.permutations(tasks):
        cost = total_cost(perm, cost_matrix)
        if cost < min_cost:
            min_cost = cost
            optimal_assignment = perm
    optimal_assignment_pairs = [(worker + 1, task + 1) for worker, task in enumerate(optimal_assignment)]
    
    return optimal_assignment_pairs, min_cost
cost_matrix1 = [
    [3, 10, 7],
    [8, 5, 12],
    [4, 6, 9]
]
optimal_assignment1, min_cost1 = assignment_problem(cost_matrix1)
print("Test Case 1")
print("Optimal Assignment:", optimal_assignment1)
print("Total Cost:", min_cost1)
print()
