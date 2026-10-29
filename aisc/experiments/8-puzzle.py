import heapq

GOAL_STATE = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

GOAL_POSITIONS = {value: idx for idx, value in enumerate(GOAL_STATE)}

def manhattan_distance(state):
    distance = 0
    for idx, value in enumerate(state):
        if value == 0:
            continue
        goal_idx = GOAL_POSITIONS[value]
        current_row, current_col = divmod(idx, 3)
        goal_row, goal_col = divmod(goal_idx, 3)
        distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

def get_neighbours(state):
    neighbours = []
    blank_idx = state.index(0)
    row, col = divmod(blank_idx, 3)

    moves = [
        (-1, 0, "up"),
        (1, 0, "down"),
        (0, -1, "left"),
        (0, 1, "right")
    ]

    for dr, dc, move_direction in moves:
        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_idx = new_row * 3 + new_col
            new_state = list(state)
            new_state[blank_idx], new_state[new_idx] = new_state[new_idx], new_state[blank_idx]
            neighbours.append((move_direction, tuple(new_state)))

    return neighbours

def a_star(start_state):
    counter = 0
    open_list = []

    heapq.heappush(
        open_list,
        (manhattan_distance(start_state), 0, counter, start_state, [])
    )

    visited = {start_state: 0}
    nodes_expanded = 0

    while open_list:
        f, g, _, current_state, path = heapq.heappop(open_list)
        nodes_expanded += 1

        if current_state == GOAL_STATE:
            return path, g, nodes_expanded

        for move, neighbour in get_neighbours(current_state):
            new_g = g + 1

            if neighbour not in visited or new_g < visited[neighbour]:
                visited[neighbour] = new_g
                new_f = new_g + manhattan_distance(neighbour)
                counter += 1

                heapq.heappush(
                    open_list,
                    (new_f, new_g, counter, neighbour, path + [(move, neighbour)])
                )

    return None, -1, nodes_expanded

def is_solvable(state):
    tiles = [x for x in state if x != 0]
    inversions = 0

    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i] > tiles[j]:
                inversions += 1

    return inversions % 2 == 0

def print_state(state):
    for i in range(0, 9, 3):
        print(" ".join(str(x) if x != 0 else "_" for x in state[i:i + 3]))
    print()

if __name__ == "__main__":

    start_state = (1, 5, 2,
                   4, 3, 0,
                   7, 8, 6)

    print("=" * 50)
    print("INITIAL STATE:")
    print_state(start_state)

    print("GOAL STATE:")
    print_state(GOAL_STATE)

    if not is_solvable(start_state):
        print("This initial state is NOT solvable.")
    else:
        print("Initial Heuristic h(n):", manhattan_distance(start_state))

        print("\n" + "=" * 50)
        print("RUNNING A* SEARCH...\n")

        solution_path, cost, expanded = a_star(start_state)

        if solution_path is None:
            print("No solution found.")
        else:
            print(f"Solution found in {cost} moves.")
            print(f"Total nodes expanded: {expanded}")

            print("\nStep-by-step solution:")
            print("-" * 30)

            print("Step 0 (Start):")
            print_state(start_state)

            for step_num, (move, state) in enumerate(solution_path, start=1):
                print(f"Step {step_num}: Move blank {move}")
                print_state(state)

    print("=" * 50)
