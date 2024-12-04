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

def sum_of_multiplications_with_conditions(file_path):
    # Read the file
    with open(file_path, 'r') as file:
        memory_content = file.read()

        instruction_pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
        
        conditional_pattern = re.compile(r".+?(?=don?'?t?\(\)|\Z)", re.DOTALL)
        memory_parts_match = conditional_pattern.findall(memory_content)
        result = sum([sum([int(instruction.group(1)) * int(instruction.group(2)) for instruction in instruction_pattern.finditer(part)]) for part in memory_parts_match if not part.startswith("don't()")])
    return result


file_path = 'input3.txt'  # Replace with your file path
result1 = sum_of_multiplications(file_path)
result2 = sum_of_multiplications_with_conditions(ile_path)
print(f"Result 1: {result1}")
print(f"Result 2: {result2}")


