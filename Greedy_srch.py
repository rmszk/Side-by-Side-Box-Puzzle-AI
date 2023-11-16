from queue import PriorityQueue
import copy

class PuzzleState:
    def __init__(self, matrix, red_block_position):
        self.matrix = matrix
        self.red_block_position = red_block_position

    def __eq__(self, other):
        return self.matrix == other.matrix and self.red_block_position == other.red_block_position

    def __hash__(self):
        return hash(str(self.matrix) + str(self.red_block_position))

    def __lt__(self, other):
        return False

def heuristic(state):
    # A simple heuristic function (you need to define your own based on your puzzle)
    return 0

def is_goal(state, exit_row, exit_col):
    return state.red_block_position == (exit_row, exit_col)

def get_neighbors(state):
    neighbors = []

    i, j = state.red_block_position

    # Move the red block right
    if j + 1 < len(state.matrix[i]):
        new_matrix = copy.deepcopy(state.matrix)
        new_matrix[i][j], new_matrix[i][j + 1] = new_matrix[i][j + 1], new_matrix[i][j]
        neighbors.append(PuzzleState(new_matrix, (i, j + 1)))

    # Move the red block left
    if j - 1 >= 0:
        new_matrix = copy.deepcopy(state.matrix)
        new_matrix[i][j], new_matrix[i][j - 1] = new_matrix[i][j - 1], new_matrix[i][j]
        neighbors.append(PuzzleState(new_matrix, (i, j - 1)))

    # Move the red block up
    if i - 1 >= 0:
        new_matrix = copy.deepcopy(state.matrix)
        new_matrix[i][j], new_matrix[i - 1][j] = new_matrix[i - 1][j], new_matrix[i][j]
        neighbors.append(PuzzleState(new_matrix, (i - 1, j)))

    # Move the red block down
    if i + 1 < len(state.matrix):
        new_matrix = copy.deepcopy(state.matrix)
        new_matrix[i][j], new_matrix[i + 1][j] = new_matrix[i + 1][j], new_matrix[i][j]
        neighbors.append(PuzzleState(new_matrix, (i + 1, j)))

    return neighbors

def find_red_block(matrix):
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == 'RED':
                return (i, j)

def greedy_search(initial_state, exit_row, exit_col):
    open_set = PriorityQueue()
    open_set.put((0, initial_state))
    closed_set = set()

    nodes_expanded = 0

    while not open_set.empty():
        _, current_state = open_set.get()

        if is_goal(current_state, exit_row, exit_col):
            return nodes_expanded

        closed_set.add(current_state)

        neighbors = get_neighbors(current_state)
        for neighbor in neighbors:
            if neighbor not in closed_set:
                priority = heuristic(neighbor)
                open_set.put((priority, neighbor))
                nodes_expanded += 1

    return nodes_expanded

def main():
    # Replace these variables with the actual puzzle configuration
    initial_matrix = [['*', '*', '*', '*', '*', '*', '*', '*'],  # 0
                      ['*', '*', '*', '*', '*', '*', '*', '*'],  # 1
                      ['*', '*', '*', '*', '*', '*', '*', '*'],  # 2
                      ['*', '*', '*', '*', '*', 'RED', '*', '*'],  # 3
                      ['*', '*', '*', '*', '*', '*', '*', '*'],  # 4
                      ['*', '*', '*', '*', '*', '*', '*', '*'],  # 5
                      ['*', '*', '*', '*', '*', '*', '*', '*'],  # 6
               # Column 0    1    2    3    4    5    6    7
                      # ... (fill the rest of the matrix)
                     ]
    exit_row, exit_col = 6, 7  # Replace with the actual exit coordinates
    initial_state = PuzzleState(initial_matrix, find_red_block(initial_matrix))

    nodes_expanded = greedy_search(initial_state, exit_row, exit_col)
    print("Nodes Expanded:", nodes_expanded)

if __name__ == "__main__":
    main()
