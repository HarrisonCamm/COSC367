def n_queens_neighbours(state):
    if not state or len(state) < 2:
        return []
    
    state_list = list(state)
    neighbours = []
    n = len(state)
    
    for i in range(n):
        for j in range(i + 1, n):  # Ensure j is always greater than i
            # Swap elements at positions i and j
            state_list[i], state_list[j] = state_list[j], state_list[i]
            
            # Convert list back to tuple and add to neighbours
            neighbours.append(tuple(state_list))
            
            # Swap elements back to original positions for next iteration
            state_list[i], state_list[j] = state_list[j], state_list[i]
    
    return sorted(neighbours)

# Test cases
print(n_queens_neighbours((1, 2)))  # [(2, 1)]
print(n_queens_neighbours((1, 3, 2)))  # [(1, 2, 3), (2, 3, 1), (3, 1, 2)]s
print(n_queens_neighbours((1, 2, 3)))  # [(1, 3, 2), (2, 1, 3), (3, 2, 1)]
print(n_queens_neighbours((1,)))  # []
