
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

def ids(initial_state, exit_row, exit_col, depth_limit=50):
    for depth in range(1, depth_limit + 1):
        result = dfs_recursive_depth_limit(initial_state, exit_row, exit_col, depth, set(), 0)
        if result is not None:
            return result

    return "Solution not found within depth limit"

def dfs_recursive_depth_limit(current_state, exit_row, exit_col, depth, closed_set, nodes_expanded):
    if is_goal(current_state, exit_row, exit_col):
        return nodes_expanded, depth

    if depth == 0:
        return None

    closed_set.add(current_state)

    neighbors = get_neighbors(current_state)
    for neighbor in neighbors:
        if neighbor not in closed_set:
            result = dfs_recursive_depth_limit(neighbor, exit_row, exit_col, depth - 1, closed_set, nodes_expanded + 1)
            if result is not None:
                return result

    return None

def main():
    #_ = '*' All Asterisk represents an Full cell
    #---------------------------Start of the Puzzle---------------------------------
    initial_matrix = [
                      ['*', '*', '*', '*', '*', '*', '*', '*'],  # 0
                      ['*', 'BS', 'RED', '*', '*', '*', '*', '*'],# 1
                      ['*', '*', '*', '*', '*', '*', '*', '*'],  # 2
                      ['*', '*', '*', '*', '*', '*', '*', '*'],  # 3
                      ['*', '*', '*', '*', '*', '*', '*', '*'],  # 4
                      ['*', '*', '*', '*', '*', '*', '*', '*'],  # 5
                      ['*', '*', '*', '*', '*', '*', '*', '*'],  # 6
               # Column 0    1    2    3    4    5    6    7
                     ]
    
    
    exit_row, exit_col = 3, 7  # actual exit coordinates
    initial_state = PuzzleState(initial_matrix, find_red_block(initial_matrix))

    nodes_expanded_ids, solution_depth = ids(initial_state, exit_row, exit_col)
    print("Nodes Expanded (IDS):", nodes_expanded_ids)
   # print(initial_matrix)
    #print(dfs_recursive_depth_limit)
    print("Solution Length:", solution_depth)

if __name__ == "__main__":
    main()
