# Read the input file and build the grid
with open("input4.txt") as fh:
    data = fh.read()

#Part 1
    
grid = {}
for y, line in enumerate(data.splitlines()):
    for x, c in enumerate(line):
        grid[complex(x, y)] = c

# Function to count occurrences of "XMAS"
def count_xmas(point, grid):
    """Count occurrences of 'XMAS' starting at the given point in all directions."""
    if grid.get(point) != "X":
        return 0
    counter = 0
    # Directions: right, diagonal-right-down, down, diagonal-left-down, etc.
    directions = [1 + 0j, 1 + 1j, 0 + 1j, -1 + 1j, -1 + 0j, -1 - 1j, 0 - 1j, 1 - 1j]
    for direction in directions:
        # Check the next three points in the direction
        points = (point + n * direction for n in range(1, 4))
        if [grid.get(pt) for pt in points] == ["M", "A", "S"]:
            counter += 1
    return counter

# Calculate total occurrences of "XMAS"
xmas_count = sum(count_xmas(point, grid) for point in grid)
print(f"Part 1 - Total 'XMAS' Count: {xmas_count}")


#Part 2 

# Function to check for specific "A" pattern
def is_masx(point, grid):
    """Check if the given point is 'A' with diagonally surrounding 'M' and 'S'."""
    if grid.get(point) != "A":
        return False
    # Check diagonal pairs
    diagonal_1 = {grid.get(point + (1 + 1j)), grid.get(point + (-1 - 1j))}
    diagonal_2 = {grid.get(point + (-1 + 1j)), grid.get(point + (1 - 1j))}
    return diagonal_1 == diagonal_2 == {"M", "S"}

# Calculate total occurrences of the "A" pattern
masx_count = sum(is_masx(point, grid) for point in grid)
print(f"Part 2 - Total 'MASX' Pattern Count: {masx_count}")
