class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l_nums = len(nums)
        left = 0
        right = l_nums - 1 
        i = 0
        while i < l_nums and right > left and i <= right:
            if nums[i] == 2:
                swp = nums[right]
                nums[right] = 2
                nums[i] = swp
                right -= 1
            elif nums[i] == 0 and left != i:
                swp = nums[right]
                swp = nums[left]
                nums[left] = 0 
                nums[i] = swp
                left += 1
            else:
                i += 1

