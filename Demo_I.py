from queue import Queue
from collections import deque
import copy

class PuzzleState:
    def __init__(self, matrix, red_block_position):
        self.matrix = matrix
        self.red_block_position = red_block_position

    def __eq__(self, other):
        return self.matrix == other.matrix and self.red_block_position == other.red_block_position

    def __hash__(self):
        return hash(str(self.matrix) + str(self.red_block_position))

def read_input(file_path):
    # Implement this function to read the puzzle configuration from the text file
    # You need to set the initial state, matrix, and red block position
    with open(file_path, 'r') as file:
        lines = file.readlines()

    matrix = [list(line.strip()) for line in lines]
    red_block_position = find_red_block(matrix)

    return PuzzleState(matrix, red_block_position)

def find_red_block(matrix):
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == 'R':
                return (i, j)

def is_goal(state, exit_row, exit_col):
    # Check if the red block is at the exit
    return state.red_block_position == (exit_row, exit_col)

def get_neighbors(state):
    # Generate possible next states by moving blocks
    neighbors = []

    # Implement logic to generate neighbors based on the rules of the puzzle
    # Move the red block up, down, left, and right

    # Example: Move red block right
    new_matrix = copy.deepcopy(state.matrix)
    i, j = state.red_block_position
    new_matrix[i][j], new_matrix[i][j + 1] = new_matrix[i][j + 1], new_matrix[i][j]
    neighbors.append(PuzzleState(new_matrix, (i, j + 1)))

    # Add other possible moves...

    return neighbors

def bfs(initial_state, exit_row, exit_col):
    # Breadth-First Search
    queue = Queue()
    queue.put(initial_state)
    visited = set()

    while not queue.empty():
        current_state = queue.get()

        if is_goal(current_state, exit_row, exit_col):
            return current_state

        visited.add(current_state)

        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                queue.put(neighbor)

def dfs(initial_state, exit_row, exit_col):
    # Depth-First Search
    stack = deque()
    stack.append(initial_state)
    visited = set()

    while stack:
        current_state = stack.pop()

        if is_goal(current_state, exit_row, exit_col):
            return current_state

        visited.add(current_state)

        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                stack.append(neighbor)

# Implement other search algorithms (UCS, IDS, A*, Greedy) similarly

def heuristic(state):
    # A simple heuristic function (you need to define your own based on your puzzle)
    return 0

def a_star(initial_state, exit_row, exit_col):
    # A* Search
    open_set = {initial_state}
    closed_set = set()

    while open_set:
        current_state = min(open_set, key=lambda x: len(x.matrix) + heuristic(x))
        open_set.remove(current_state)

        if is_goal(current_state, exit_row, exit_col):
            return current_state

        closed_set.add(current_state)

        for neighbor in get_neighbors(current_state):
            if neighbor not in closed_set:
                open_set.add(neighbor)

def main():
    file_path = "input.txt"  # Replace with your input file path
    exit_row, exit_col = 6, 7  # Replace with the actual exit coordinates
    initial_state = read_input(file_path)

    # Run each search algorithm
    bfs_result = bfs(initial_state, exit_row, exit_col)
    dfs_result = dfs(initial_state, exit_row, exit_col)
    a_star_result = a_star(initial_state, exit_row, exit_col)

    # Print results for each search algorithm
    print("BFS:", bfs_result.matrix)
    print("DFS:", dfs_result.matrix)
    print("A*:", a_star_result.matrix)

if __name__ == "__main__":
    main()
