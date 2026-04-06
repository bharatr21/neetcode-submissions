from bisect import bisect_left, bisect_right
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        inits = [matrix[i][0] for i in range(m)]
        a = bisect_left(inits, target)
        a = a - 1 if a > 0 and matrix[a][0] > target else a
        print(matrix[a])
        b = bisect_left(matrix[a], target)
        return matrix[a][b] == target
