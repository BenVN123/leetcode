# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        res = 0
        def traverse(node, p=False, gp=False):
            nonlocal res

            if not node:
                return
            
            if gp:
                res += node.val
            
            traverse(node.left, p=node.val % 2 == 0, gp=p)
            traverse(node.right, p=node.val % 2 == 0, gp=p)
        
        traverse(root)
        return res
        
