class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        l_nums = len(nums)
        if l_nums == 1:
            return True 
        left = 1 
        right = 2 
        prev = nums[1] - nums[0] 
        if prev not in [-1, 1, 2]:
            return False

        while right < l_nums:
            diff = nums[right] - nums[left]
            if diff in [1,2,3,-1]:
                if diff == -1 and prev == -1:
                    return False
                elif diff == 3 and prev != -1:
                    return False
            else:
                return False
            prev = diff 
            left += 1
            right += 1
        return True
