class Solution:
    def decodeString(self, s: str) -> str:
        def decode(s):
            left = 0
            right = 1
            res = ""
            while right <= len(s):
                if s[left].isalpha():
                    res += s[left]
                    left += 1
                    right += 1
                elif s[left] == "]":
                    return res, left + 2 
                else:
                    while s[right] != "[":
                        right += 1
                    repeat_count = int(s[left:right])
                    substring, add_left = decode(s[right + 1:])
                    left = right + add_left
                    res += substring * repeat_count
                    right = left + 1

            return res

        return decode(s)
