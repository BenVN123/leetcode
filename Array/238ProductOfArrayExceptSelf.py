class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        product = 1
        l_nums = len(nums)
        for i in nums:
            product *= i
            pre.append(product) 

        post = [1] * l_nums
        product = 1
        for i in range(l_nums - 1, -1, -1):
            product *= nums[i] 
            post[i] = product

        res = [post[1]]
        product = 1
        for i in range(1, l_nums - 1):
            res.append(post[i + 1] * pre[i - 1])
        res.append(pre[l_nums - 2])

        return res
