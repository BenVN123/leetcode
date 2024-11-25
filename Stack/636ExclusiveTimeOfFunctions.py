class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = collections.deque()

        prev_id, prev_action, prev_time = logs[0].split(":") 
        stack.append(int(prev_id))
        prev_time = int(prev_time)
        for i in range(1, len(logs)):
            id, action, time = logs[i].split(":") 
            id = int(id)
            time = int(time)

            if stack:
                if action == "end":
                    if prev_action == "start":
                        res[id] += time - prev_time + 1
                    else:
                        res[id] += time - prev_time
                    stack.pop()
                else:
                    if prev_action == "end":
                        res[stack[-1]] += time - prev_time - 1
                    else:
                        res[stack[-1]] += time - prev_time
                    stack.append(id)
            else:
                stack.append(id)

            prev_time = time
            prev_action = action
        
        return res

