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



print(n_queens_cost((1, 2)))
