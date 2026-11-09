# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # recursive
        
        if head == None:
            return head
        
        def func(prev , current):
            # base func
            if current.next == None:
                current.next = prev
                return current
            else:
                ans = func(current, current.next)
                current.next = prev
            return ans
        
        return func(None, head)

       