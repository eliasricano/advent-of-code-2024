def get_levels_lists(filename):
    with open(filename) as file:
        levels = []
        for line in file:
            arr = []
            for num in line.split():
                arr.append(int(num))
            levels.append(arr)
    return levels

def close_nums(num1, num2):
    difference = abs(num1 - num2)
    return 1 <= difference <= 3

def is_increasing(level):
    return all(
        (level[i] < level[i + 1]) and 
        close_nums(level[i + 1], level[i]) 
        for i in range(len(level) - 1)
        )

def is_decreasing(level):
        return all(
        (level[i] > level[i + 1]) and 
        close_nums(level[i + 1], level[i]) 
        for i in range(len(level) - 1)
        )

levels = get_levels_lists('input.txt')
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
safe_count = 0

for level in levels:
    if is_increasing(level) or is_decreasing(level):
        safe_count += 1

print(safe_count)