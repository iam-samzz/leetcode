# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #floyd cycle detection algo
        p = head
        q = head

        while p!= None and p.next != None:
            p = p.next.next
            q = q.next

            if p == q: # loop found
                
                q = head
                while q != p:
                    p = p.next
                    q = q.next
                return p
        return None