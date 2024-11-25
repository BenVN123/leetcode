class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_check(idx, l, r):
            nonlocal s
            left = l 
            right = r
            while left > -1 and right < len(s) and s[right] == s[left]:
                left -= 1
                right += 1
            return (right - 1) - left, s[left + 1:right]

        res = "" 
        res_len = 0
        for i in range(len(s)):
            for l, r in (expand_check(i, i - 1, i + 1), expand_check(i, i, i + 1)):
                if l > res_len:
                    res_len = l
                    res = r

        return res
