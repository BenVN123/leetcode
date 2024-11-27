class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        seen = [False] * numCourses
        enrolled = [False] * numCourses
        preq = {}
        res = []

        for p in prerequisites:
            if preq.get(p[0]):
                preq[p[0]].append(p[1])    
            else:
                preq[p[0]] = [p[1]]

        def check_classes(course):
            if seen[course]:
                return False
            if enrolled[course]: 
                return True

            seen[course] = True 

            for p in preq.get(course, []):
                if not enrolled[p]:
                    if not check_classes(p):
                        return False

            enrolled[course] = True
            seen[course] = False 
            res.append(course)
            return True 

        for i in range(numCourses):
            if not check_classes(i):
                return []
            
        return res
