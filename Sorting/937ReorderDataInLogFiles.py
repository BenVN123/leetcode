class LetterLog(object):
    def __init__(self, log):
        self.log = log
        i = 0
        while log[i] != " ":
            i += 1
        self.id = log[:i]
        self.content = log[i + 1:] 

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        heap = []
        digit_idx = []
        heap_length = 0
        res = []

        for idx, log in enumerate(logs):
            if not log[-1].isalpha():
                digit_idx.append(idx)
                continue
            log_obj = LetterLog(log)
            i = 0
            while i < heap_length:
                if log_obj.content < heap[i].content:
                    break
                elif log_obj.content == heap[i].content:
                    if log_obj.id < heap[i].id:
                        break 
                i += 1
            heap.insert(i, log_obj)
            heap_length += 1

        for i in heap:
            res.append(i.log)
        for i in digit_idx:
            res.append(logs[i]) 

        return res
