def find_max_value(matrix):
    max_value=0
    for row in matrix:
        max_value=max(row)
    return max_value


matrix = [
    [3, 7, 1, 2],
    [8, 5, 6, 4],
    [2, 1, 8, 99]
]
max_value = find_max_value(matrix)
print("\nMaximum Value:", max_value)