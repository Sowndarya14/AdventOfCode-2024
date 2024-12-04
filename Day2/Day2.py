# def safety(reports):
# #check if increasing or decreasing
#     def is_sorted(lst):
#         if lst == sorted(lst) or lst == sorted(lst, reverse=True):
#             return True
#         return False

#     def check_diff(lst):
#         for i in range(0,len(lst)-1):
#             if abs(lst[i] - lst[i+1]) > 0 and abs(lst[i] - lst[i+1]) <= 3:
#                 continue
#             else:
#                 return False
#         return True

#     count = 0
#     for lst in reports:
#         cond1 = is_sorted(lst)
#         cond2 = check_diff(lst)

#         if cond1 == True and cond2 == True:
#             count += 1
#         else:
#             continue
#     print(count)     
#     return count



def is_safe(levels):
    """
    Check if the sequence is safe and return the index of the first unsafe level if any.
    :param levels: A list of integers representing levels.
    :return: Index of the first unsafe level or None if safe.
    """
    increasing = False
    previous = 0

    for index, level in enumerate(levels):
        if index == 0:
            previous = level
            continue
        elif index == 1:
            increasing = level > previous

        if abs(level - previous) not in range(1, 4):
            return index

        if increasing:
            if level < previous:
                return index
        else:
            if level > previous:
                return index

        previous = level

    return None


def part1(input_lines):
    """
    Process the input and calculate the sum based on the rules for part 1.
    :param input_lines: A list of lists or strings representing input levels.
    :return: Result as an integer.
    """
    result = 0
    for line in input_lines:
        if isinstance(line, list):  # Input is a list of lists
            levels = line
        else:  # Input is a list of strings
            levels = list(map(int, line.split()))

        if is_safe(levels) is None:
            result += 1
    return result


def part2(input_lines):
    """
    Process the input and calculate the sum based on the rules for part 2.
    :param input_lines: A list of lists or strings representing input levels.
    :return: Result as an integer.
    """
    result = 0
    for line in input_lines:
        if isinstance(line, list):  # Input is a list of lists
            levels = line
        else:  # Input is a list of strings
            levels = list(map(int, line.split()))

        unsafe_index = is_safe(levels)
        if unsafe_index is not None:
            for i in range(unsafe_index, -1, -1):
                filtered_levels = [level for j, level in enumerate(levels) if j != i]
                if is_safe(filtered_levels) is None:
                    result += 1
                    break
            else:
                result += 0
        else:
            result += 1
    return result


# Open the file in read mode
with open('input2.txt', 'r') as file:
    reports = []
    for line in file:
        # Convert the line to a list of integers
        numbers = list(map(int, line.split()))
        reports.append(numbers)


print(part1(reports))
print(part2(reports))
