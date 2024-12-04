import re
# Part 1 of Day 3
def sum_of_multiplications(file_path):
    # Step 1: Read the file
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Step 2: Find all matches for mul(a,b)
    matches = re.findall(r"mul\((\d+),(\d+)\)", content)  # Extract numbers inside mul(a,b)
    
    # Step 3: Calculate the sum of products
    total_sum = sum(int(a) * int(b) for a, b in matches)
    
    return total_sum


#Part2 of Day 3

import re

def sum_of_multiplications_with_conditions(file_path):
    # Read the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Initialize state
    enabled = True
    total_sum = 0

    # Regex to find instructions
    # Matches mul(a, b), do(), and don't()
    instructions = re.findall(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", content)

    # Process instructions
    for instr in instructions:
        if instr[0] and instr[1]:  # This is a mul(a, b) instruction
            if enabled:
                total_sum += int(instr[0]) * int(instr[1])
        elif "do()" in instr:  # This is a do() instruction
            enabled = True
        elif "don't()" in instr:  # This is a don't() instruction
            enabled = False

    return total_sum


file_path = 'input3.txt'  # Replace with your file path
result1 = sum_of_multiplications(file_path)
result2 = sum_of_multiplications_with_conditions(file_path)
print(f"Result 1: {result1}")
print(f"Result 2: {result2}")
