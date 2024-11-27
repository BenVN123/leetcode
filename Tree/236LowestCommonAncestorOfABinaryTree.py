# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(node):
            nonlocal p, q
            if not node:
                return None, 0 
            
            left_found, l_count = find(node.left)
            if left_found: 
                return left_found, 2

            right_found, r_count = find(node.right)
            if right_found:
                return right_found, 2

            if (node.val == p.val or node.val == q.val):
                if (l_count == 1 or r_count == 1):
                    return node, 2
                return None, 1 
            elif l_count == r_count == 1: 
                return node, 2 
            elif l_count == 1 or r_count == 1:
                return None, 1

            return None, 0 

        return find(root)[0]
