# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:


        # cycle detection algorithm
        p = head
        q = head
        
        while p!= None and p.next != None:
            q = q.next
            p = p.next.next
            if p == q:
                return True
        return False