from collections import deque
import copy
import time  # Import time module to measure execution time

def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_valid(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
    for x in range(9):
        if grid[x][col] == num:
            return False
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for x in range(3):
        for y in range(3):
            if grid[start_row + x][start_col + y] == num:
                return False
    return True

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None  

def bfs_solve(grid):
    queue = deque()
    queue.append(grid)
    while queue:
        current_grid = queue.popleft()
        empty_cell = find_empty(current_grid)
        if not empty_cell:
            return current_grid  
        else:
            row, col = empty_cell
            for num in range(1, 10):
                if is_valid(current_grid, row, col, num):
                    new_grid = copy.deepcopy(current_grid)
                    new_grid[row][col] = num
                    queue.append(new_grid)
    return None 


def backtrack_solve(grid):
    empty_cell = find_empty(grid)
    if not empty_cell:
        return True 
    else:
        row, col = empty_cell
        for num in range(1, 10):
            if is_valid(grid, row, col, num):
                grid[row][col] = num
                if backtrack_solve(grid):
                    return True
                grid[row][col] = 0  
        return False  
# Main function
def main():
   

    # Easy Level
    easy_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],  # Row 1
        [6, 0, 0, 1, 9, 5, 0, 0, 0],  # Row 2
        [0, 9, 8, 0, 0, 0, 0, 6, 0],  # Row 3
        [8, 0, 0, 0, 6, 0, 0, 0, 3],  # Row 4
        [4, 0, 0, 8, 0, 3, 0, 0, 1],  # Row 5
        [7, 0, 0, 0, 2, 0, 0, 0, 6],  # Row 6
        [0, 6, 0, 0, 0, 0, 2, 8, 0],  # Row 7
        [0, 0, 0, 4, 1, 9, 0, 0, 5],  # Row 8
        [0, 0, 0, 0, 8, 0, 0, 7, 9]   # Row 9
    ]

    # Medium Level
    medium_grid = [
        [0, 0, 0, 0, 6, 0, 5, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 7, 0, 0, 9, 0, 0, 2],
        [0, 5, 0, 0, 0, 0, 0, 7, 0],
        [6, 0, 0, 4, 0, 0, 9, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 1, 0, 9, 0, 0, 0, 0]
    ]

    # Hard Level
    hard_grid = [
        [0, 0, 0, 6, 0, 0, 4, 0, 0],
        [7, 0, 0, 0, 0, 3, 6, 0, 0],
        [0, 0, 0, 0, 9, 1, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 1, 8, 0, 0, 0, 3],
        [0, 0, 0, 3, 0, 6, 0, 4, 5],
        [0, 4, 0, 2, 0, 0, 0, 6, 0],
        [9, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 1, 0, 0]
    ]

    difficulty = input("Choose difficulty level (Easy/Medium/Hard): ").strip().lower()
    if difficulty == "easy":
        grid = easy_grid
    elif difficulty == "medium":
        grid = medium_grid
    elif difficulty == "hard":
        grid = hard_grid
    else:
        print("Invalid difficulty level.")
        return

    print("\nInitial Sudoku Grid:")
    print_grid(grid)

    print("\nSolving with BFS...")
    bfs_start_time = time.time()  
    solution_bfs = bfs_solve(grid)
    bfs_end_time = time.time()  
    bfs_time = bfs_end_time - bfs_start_time  
    if solution_bfs:
        print("BFS Solution:")
        print_grid(solution_bfs)
        print(f"BFS solved the puzzle in {bfs_time:.6f} seconds.")
    else:
        print("No solution found using BFS.")
        print(f"BFS terminated after {bfs_time:.6f} seconds.")

    # Solve using Backtracking
    print("\nSolving with Backtracking...")
    grid_copy = copy.deepcopy(grid)
    backtrack_start_time = time.time()
    if backtrack_solve(grid_copy):
        backtrack_end_time = time.time()
        backtrack_time = backtrack_end_time - backtrack_start_time  # Total time
        print("Backtracking Solution:")
        print_grid(grid_copy)
        print(f"Backtracking solved the puzzle in {backtrack_time:.6f} seconds.")
    else:
        backtrack_end_time = time.time()
        backtrack_time = backtrack_end_time - backtrack_start_time  # Total time
        print("No solution found using Backtracking.")
        print(f"Backtracking terminated after {backtrack_time:.6f} seconds.")


if __name__ == "__main__":
    main()

