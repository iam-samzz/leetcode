#Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:

        prev = None
        current = head

        while current != None:
            # create a temp to track next element
            temp = current.next

            #cut the current bond and points to prev element
            current.next = prev

            # shift the prev pointer to current pointer
            prev = current

            # move the  current to temp. i.e the next element
            current = temp
        return prev
            

    
