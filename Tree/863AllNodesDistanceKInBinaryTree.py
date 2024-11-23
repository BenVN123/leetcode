# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]

        res = [] 
        def helper(node: TreeNode, distance: int = -1):
            nonlocal res, target, k
            if not node:
                return -1

            if node == target:
                helper(node.left, 0) 
                helper(node.right, 0)


                return 0
            elif distance != -1: 
                if distance + 1 == k:
                    res.append(node.val)
                else:
                    helper(node.left, distance + 1)
                    helper(node.right, distance + 1)
                    return distance + 1
            else:
                left_dist = helper(node.left)
                right_dist = helper(node.right) 

                if left_dist != -1:
                    if left_dist + 1 == k:
                        res.append(node.val)
                    else:
                        if node.right:
                            helper(node.right, left_dist + 1)
                        return left_dist + 1
                if right_dist != -1:
                    if right_dist + 1 == k:
                        res.append(node.val)
                    else:
                        if node.left:
                            helper(node.left, right_dist + 1)
                        return right_dist + 1

                return -1

        helper(root)
        return res
