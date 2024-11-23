class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q1 = collections.deque()
        q2 = collections.deque()

        orange_count = 0
        rotten_count = 0
        row_count = len(grid)
        col_count = len(grid[0]) 
        for row in range(row_count):
            for col in range(col_count):
                cell = grid[row][col]
                if cell != 0:
                    orange_count += 1
                    if cell == 2:
                        q1.append([row, col])
                        rotten_count += 1

        minutes = -1 
        while q1:
            minutes += 1
            while q1:
                cell = q1.popleft()
                for d in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    row = cell[0] + d[0]
                    col = cell[1] + d[1]
                    if row >= 0 and row < row_count and col >= 0 and col < col_count and grid[row][col] == 1:
                        grid[row][col] = 2
                        q2.append([row, col]) 
                        rotten_count += 1
            q1 = q2
            q2 = collections.deque()
        if orange_count > rotten_count:
            return -1
        return max(0, minutes)
