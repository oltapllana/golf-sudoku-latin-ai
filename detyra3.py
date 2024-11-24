import time

def iddfs_latin_square(n):
    """
    Generates a Latin Square using Iterative Deepening Depth-First Search (IDDFS).
    
    Parameters:
        n (int): The order of the Latin Square (n x n).
    
    Returns:
        list: A 2D list representing the Latin Square if found, else None.
    """
    max_depth = n * n

    for depth_limit in range(1, max_depth + 1):

        grid = [[0] * n for _ in range(n)]
        
        row_sets = [set() for _ in range(n)]
        

        col_sets = [set() for _ in range(n)]
        
        if iddfs_dls(grid, row_sets, col_sets, 0, depth_limit, n):
            return grid  

    return None

def iddfs_dls(grid, row_sets, col_sets, cell_index, depth_limit, n):
    """
    Performs Depth-Limited Search (DLS) for IDDFS.
    
    Parameters:
        grid (list): The current state of the Latin Square grid.
        row_sets (list): List of sets tracking used numbers in each row.
        col_sets (list): List of sets tracking used numbers in each column.
        cell_index (int): The current cell index being filled (0 to n*n - 1).
        depth_limit (int): The current depth limit for IDDFS.
        n (int): The order of the Latin Square.
    
    Returns:
        bool: True if a solution is found, else False.
    """

    if cell_index == n * n:
        return True
    

    if cell_index >= depth_limit:
        return False
    

    row = cell_index // n
    col = cell_index % n
    
    for num in range(1, n + 1):

        if num not in row_sets[row] and num not in col_sets[col]:

            grid[row][col] = num

            row_sets[row].add(num)
            col_sets[col].add(num)

            if iddfs_dls(grid, row_sets, col_sets, cell_index + 1, depth_limit, n):
                return True
            
            grid[row][col] = 0
            row_sets[row].remove(num)
            col_sets[col].remove(num)
    
    return False

def backtracking_latin_square(n):
    """
    Generates a Latin Square using Backtracking.
    
    Parameters:
        n (int): The order of the Latin Square (n x n).
    
    Returns:
        list: A 2D list representing the Latin Square if found, else None.
    """

    grid = [[0] * n for _ in range(n)]

    row_sets = [set() for _ in range(n)]
    
    col_sets = [set() for _ in range(n)]

    if backtracking_fill(grid, row_sets, col_sets, 0, n):
        return grid 

    return None 

def backtracking_fill(grid, row_sets, col_sets, cell_index, n):
    """
    Recursively fills the grid using Backtracking.
    
    Parameters:
        grid (list): The current state of the Latin Square grid.
        row_sets (list): List of sets tracking used numbers in each row.
        col_sets (list): List of sets tracking used numbers in each column.
        cell_index (int): The current cell index being filled (0 to n*n - 1).
        n (int): The order of the Latin Square.
    
    Returns:
        bool: True if a solution is found, else False.
    """
    if cell_index == n * n:
        return True
    
    row = cell_index // n
    col = cell_index % n
 
    for num in range(1, n + 1):

        if num not in row_sets[row] and num not in col_sets[col]:
            grid[row][col] = num
            
            row_sets[row].add(num)
            col_sets[col].add(num)

            if backtracking_fill(grid, row_sets, col_sets, cell_index + 1, n):
                return True 
            
            grid[row][col] = 0
            row_sets[row].remove(num)
            col_sets[col].remove(num)

    return False

def print_latin_square(grid):
    """
    Prints the Latin Square in a readable format.
    
    Parameters:
        grid (list): The Latin Square grid to be printed.
    """
    for row in grid:
        print(' '.join(map(str, row)))
def main():
    """
    The main function to execute both IDDFS and Backtracking methods for Latin Square generation.
    It measures and prints the execution time for each method.
    """
    try:
        n = int(input("Enter the order 'n' of the Latin Square (e.g., 5 for a 5x5 grid): "))
        
        if n <= 0:
            print("Please enter a positive integer for 'n'.")
            return
        
        print("\n--- Generating Latin Square using IDDFS ---")

        start_time_iddfs = time.perf_counter()
        
        iddfs_solution = iddfs_latin_square(n)

        end_time_iddfs = time.perf_counter()

        elapsed_time_iddfs = end_time_iddfs - start_time_iddfs

        if iddfs_solution:
            print("\nLatin Square generated using IDDFS:")
            print_latin_square(iddfs_solution)
        else:
            print("No solution found using IDDFS.")

        print(f"Time taken by IDDFS: {elapsed_time_iddfs:.6f} seconds")
        
        print("\n--- Generating Latin Square using Backtracking ---")
        
        start_time_backtracking = time.perf_counter()
        
        backtracking_solution = backtracking_latin_square(n)
        
        end_time_backtracking = time.perf_counter()
        
        elapsed_time_backtracking = end_time_backtracking - start_time_backtracking

        if backtracking_solution:
            print("\nLatin Square generated using Backtracking:")
            print_latin_square(backtracking_solution)
        else:
            print("No solution found using Backtracking.")
        
        print(f"Time taken by Backtracking: {elapsed_time_backtracking:.6f} seconds")
    
    except ValueError:
        print("Invalid input! Please enter a valid integer for 'n'.")

if __name__ == "__main__":
    main()