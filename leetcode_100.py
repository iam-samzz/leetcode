from typing import Optional, List

'''Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        #basically, 2 trees are same if their traversal list is same right?
        #so lets do inorder traversal on both the tree and check if the tree is same or not


        def list_check(l1,l2):

            if len(l1) != len(l2):
                return False
            
            if len(l1) == 0 and len(l2) == 0:
                return True
            x = l1.pop(0)
            y = l2.pop(0)

            if x == y:
                status = list_check(l1,l2)
                return status
            else:
                return False
            
        def inorder(root,l):

            if root == None:
                return
            #left
            inorder(root.left,l)

            #middle
            l.append(root.val)

            #right
            inorder(root.right,l)

            return l

        p_inorder = inorder(p,[])
        q_inorder = inorder(q,[])


        if list_check(p_inorder,q_inorder):
            return True
        else:
            return False

        
