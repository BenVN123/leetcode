class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row_count = len(grid)
        if row_count == 0:
            return 0
        col_count = len(grid[0]) 
        seen = [[False for i in range(col_count)] for j in range(row_count)]
        res = 0

        def dfs(row, col):
            if grid[row][col] == "0" or seen[row][col] == True:
                return 0 
            seen[row][col] = True 

            for d in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                r = row + d[0]
                c = col + d[1]
                if r >= 0 and r < row_count and c >= 0 and c < col_count:
                    dfs(r, c) 
            return 1

        for row in range(row_count):
            for col in range(col_count):
                res += dfs(row, col)
                
        return res
