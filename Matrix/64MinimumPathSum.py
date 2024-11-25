class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row_count = len(grid)
        col_count = len(grid[0])
        cost = [[sys.maxsize for i in range(col_count)] for j in range(row_count)]
        q = collections.deque()
        q.append([0, 0])
        cost[0][0] = grid[0][0]

        while q:
            q_len = len(q)
            while q_len > 0:
                cell = q.popleft()
                q_len -= 1
                
                for d in [[0, 1], [1, 0]]:
                    row = cell[0] + d[0]
                    col = cell[1] + d[1]

                    if row >= 0 and row < row_count and col >= 0 and col < col_count and cost[cell[0]][cell[1]] + grid[row][col] < cost[row][col]:
                        cost[row][col] = cost[cell[0]][cell[1]] + grid[row][col]
                        q.append([row, col])
        return cost[row_count - 1][col_count - 1]
                    

