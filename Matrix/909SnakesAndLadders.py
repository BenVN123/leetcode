class Solution:
    def get_loc(self, n, i):
        row = n - 1 - (i - 1) // n 
        col = (i - 1) % n
        if (i - 1) // n % 2 == 1:
            col = n - 1 - col
        return [row, col]

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        if n * n < 8:
            return 1
        q1 = collections.deque()
        q2 = collections.deque()

        dp = [False] * (n * n)

        q1.append(1)
        
        count = 0 
        while q1:
            while q1:
                val = q1.popleft()
                lo = self.get_loc(n, val)
                if val == n * n:
                    return count
                for i in range(val + 1, min(n * n + 1, val + 7)):
                    lo2 = self.get_loc(n, i)
                    jump_val = board[lo2[0]][lo2[1]]
                    print(jump_val)
                    print(lo2)
                    if jump_val != -1:
                        if not dp[jump_val - 1]:
                            q2.append(jump_val)
                            dp[jump_val - 1] = True
                    else:
                        if not dp[i - 1]:
                            q2.append(i)
                            dp[i - 1] = True
            q1 += q2
            q2 = collections.deque()
            count += 1
        return -1
