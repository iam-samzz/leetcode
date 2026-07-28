# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        def func(heada, headb):
            p1 = heada
            p2 = headb

            has = {}
            
            while p1!= None:

                if p1 in has:
                    return p1
                else:
                    has[p1] = p1.val
                    p1 = p1.next

            while p2 != None:
                if p2 in has:
                    return p2
                else:
                    has[p2] = p2.val
                    p2 = p2.next
                
            return None
        return func(headA,headB)