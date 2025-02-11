import os
import time

# Define grid size
ROWS, COLS = 10, 10

# Initialize the grid with a simple pattern
def create_grid():
    grid = [[0] * COLS for _ in range(ROWS)]

    # Example: Glider pattern
    grid[1][2] = 1
    grid[2][3] = 1
    grid[3][1] = 1
    grid[3][2] = 1
    grid[3][3] = 1

    return grid

# Print the grid to the console
def display_grid(grid):
    # os.system("cls" if os.name == "nt" else "clear")  # Clear screen for better visualization
    for row in grid:
        print(" ".join("#" if cell else "-" for cell in row))  # Display alive cells as "■", dead as "·"
    print("\n")

# Count live neighbors of a cell
def count_live_neighbors(grid, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] == 1:
            count += 1
    
    return count

# Compute the next generation of the grid
def next_generation(grid):
    new_grid = [[0] * COLS for _ in range(ROWS)]

    for x in range(ROWS):
        for y in range(COLS):
            live_neighbors = count_live_neighbors(grid, x, y)

            if grid[x][y] == 1:
                # A live cell survives only with 2 or 3 live neighbors
                new_grid[x][y] = 1 if live_neighbors in (2, 3) else 0
            else:
                # A dead cell becomes alive if it has exactly 3 live neighbors
                new_grid[x][y] = 1 if live_neighbors == 3 else 0

    return new_grid

# Main function to run the simulation
def main():
    grid = create_grid()

    generations = 10  # Number of generations to simulate
    for _ in range(generations):
        display_grid(grid)
        grid = next_generation(grid)  # Compute next state
        time.sleep(0.5)  # Pause to animate the game

if __name__ == "__main__":
    main()
