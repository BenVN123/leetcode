class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last = {}
        s_len = len(s)
        for i in range(s_len - 1, -1, -1): 
            if not last.get(s[i]):
                last[s[i]] = i 
        
        res = []
        curr_last = 0
        curr_start = 0 
        for i in range(s_len):
            curr_last = max(last[s[i]], curr_last)
            if i == curr_last:
                res.append(curr_last - curr_start + 1)
                curr_start = curr_last + 1

        return res
