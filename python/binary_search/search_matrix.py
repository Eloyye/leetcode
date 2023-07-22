from typing import List

#You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    #my approach is to first correctly guess the row and then to do binary search on columns
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    guess_row = 0
    while bottom >= top:
        guess_row = (bottom + top) // 2
        if matrix[guess_row][0] <= target and matrix[guess_row][len(matrix[0]) - 1] >= target:
            break
        elif matrix[guess_row][0] < target:
            top = guess_row + 1
        else:
            bottom = guess_row - 1
    while right >= left:
        guess_col = (right + left) // 2
        if matrix[guess_row][guess_col] == target:
            return True
        elif matrix[guess_row][guess_col] < target:
            left = guess_col + 1
        else:
            right = guess_col - 1
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
for val in matrix:
    print(val)
searchMatrix(matrix, 11)