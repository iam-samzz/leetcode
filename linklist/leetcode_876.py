# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        
        p = head
        q = head

        while q!= None  and q.next != None:
            q = q.next.next
            p = p.next
        return p