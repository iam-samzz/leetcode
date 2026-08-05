# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        def func(l1,l2):
            #FINDING THE CORRECT VALUE OF L1

            pointer = l1
            power = 0
            result_l1 = 0

            while pointer != None:
                result_l1 = (result_l1) + ((pointer.val) * (10**power))
                power += 1
                pointer = pointer.next
            

            #FINDING THE CORRECT VALUE OF L2
            result_l2 = 0
            pointer = l2
            power = 0

            while pointer != None:
                result_l2 = (result_l2) + ((pointer.val)*(10**power))
                power += 1
                pointer = pointer.next
            

            #ADDING L1 AND L2
            result = result_l1 + result_l2
            
            n = ListNode(result%10)
            head = n
            pointer = n
            result = result // 10
            #lets make the link list
            while result!= 0:
                n = ListNode(result%10)
                result = result // 10
                pointer.next = n
                pointer = pointer.next

            return head



            '''digit = 0
            while result != 0:
                result = result // 10
                digit += 1
            
            result = result_l1 + result_l2
            power = digit - 1
            original_result = 0
            while power >=0:
                original_result = original_result + ((result%10) * (10**power))
                power -= 1
                result = result // 10
            
            
            # found the result value..now lets change to link list
            '''
            

        return func(l1,l2)


