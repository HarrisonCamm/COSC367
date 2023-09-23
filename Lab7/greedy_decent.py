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
    
#Test Cases
def cost(x):
    return x**2

def neighbours(x):
    return [x - 1, x + 1]

for state in greedy_descent(-6.75, neighbours, cost):
    print(state)
    
    
def cost(x):
    return x**2

def neighbours(x):
    return [x - 1, x + 1]

for state in greedy_descent(-6.75, neighbours, cost):
    print(state)    