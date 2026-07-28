# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        def func(head):
            index = 0
            p1 = head
            has = {}
            
            while p1 != None:

                if p1 in has:
                    return True
                has[p1] = index

                p1 = p1.next
            return False
        return func(head)
