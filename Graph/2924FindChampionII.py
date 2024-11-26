class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        champion = -1
        weaker = [False] * n

        for edge in edges:
            if not weaker[edge[1]]:
                weaker[edge[1]] = True

        for i in range(n):
            if not weaker[i]:
                if champion == -1:
                    champion = i 
                elif champion != i: 
                    return -1 

        return champion 
