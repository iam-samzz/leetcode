# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        

        def function(head):
            slow = head
            fast = head
            
            left_list = []
            right_list = []

            #1st half list
            while fast != None and fast.next != None:
                left_list.append(slow.val)
                fast = fast.next.next
                slow = slow.next

            #2nd half list
            if fast != None:
                slow = slow.next

            while slow != None:
                right_list.append(slow.val)
                slow = slow.next
            if left_list == right_list[::-1]:
                return True
            else:
                return False
        return function(head)