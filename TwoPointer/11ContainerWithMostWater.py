class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0
        while right > left:
            res = max(res, (right - left) * min(height[right], height[left]))
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return res
