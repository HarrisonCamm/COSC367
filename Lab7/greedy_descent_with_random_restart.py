import random

def n_queens_cost(state):
    n = len(state)
    conflicts = 0
    for i in range(n):
        for j in range(i+1, n):
            dy = abs(i - j)
            dx = abs(state[i] - state[j])
            if dx == dy:
                conflicts += 1
    return conflicts


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


def greedy_descent(initial_state, neighbours, cost):
    current_state = initial_state
    path = [initial_state]
    
    while True:
        state_neighbours = neighbours(current_state)
        if not state_neighbours:
            return path
        min_neighbour = min(state_neighbours, key=cost)
        if cost(min_neighbour) < cost(current_state):
            path.append(min_neighbour)
            current_state = min_neighbour
        else:
            break
    return path


def greedy_descent_with_random_restart(random_state, neighbours, cost):
    initial_state = random_state()
    global_min = float("inf")
    
    while True:
        path = greedy_descent(initial_state,neighbours,cost)
        for state in path:
            print(state)
            if cost(state) < global_minimum:
                global_minimum = cost(state)
            
        if global_min == 0:
            break
        
        print("RESTART")
        initial_state = random_state()




N = 6
random.seed(0)

def random_state():
    return tuple(random.sample(range(1,N+1), N))   

greedy_descent_with_random_restart(random_state, n_queens_neighbours, n_queens_cost)

