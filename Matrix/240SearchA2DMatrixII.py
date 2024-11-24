class Solution:
    def binarySearch(self, l, t):
        if not l:
            return False
        length = len(l)
        mid = length // 2
        if l[mid] == t:
            return True
        elif l[mid] < t:
            return self.binarySearch(l[mid + 1:], t)
        else:
            return self.binarySearch(l[:mid], t)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        len_row = len(matrix)
        len_col = len(matrix[0])
        max_col = len_col 
        max_row = len_row
        for i in range(len_col):
            if matrix[0][i] > target:
                max_col = i 
                break
            elif matrix[0][i] == target:
                return True
        for i in range(len_row):
            if matrix[i][0] > target:
                max_row = i
                break
            elif matrix[i][0] == target:
                return True
        
        for row in range(1, max_row):
            if self.binarySearch(matrix[row][1:max_col], target):
                return True
        return False


