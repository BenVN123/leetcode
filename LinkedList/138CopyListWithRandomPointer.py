"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        og = head
        curr = head
        new_head = Node(head.val)
        new_curr = new_head
        new_ptrs = {curr: new_curr}
        while curr.next:
            new_curr.next = Node(curr.next.val)
            new_curr = new_curr.next 
            curr = curr.next
            new_ptrs[curr] = new_curr
            
        curr = head
        new_curr = new_head
        while curr:
            if curr.random:
                new_curr.random = new_ptrs[curr.random]
            curr = curr.next
            new_curr = new_curr.next

        return new_head
