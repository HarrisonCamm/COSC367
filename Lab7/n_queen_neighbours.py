def n_queens_neighbours(state):
    if not state or len(state) < 2:
        return []
    
    state_list = list(state)
    neighbours = []
    n = len(state)
    
    for i in range(n):
        for j in range(i + 1, n):  
            
            state_list[i], state_list[j] = state_list[j], state_list[i]
            
            neighbours.append(tuple(state_list))
            
            state_list[i], state_list[j] = state_list[j], state_list[i]
    
    return sorted(neighbours)


# Test cases
print(n_queens_neighbours((1, 2)))
print(n_queens_neighbours((1, 3, 2)))
print(n_queens_neighbours((1, 2, 3)))
print(n_queens_neighbours((1,)))
