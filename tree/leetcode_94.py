#Given the root of a binary tree, return the inorder traversal of its nodes' values.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self,root):

        result = []

        def inorder(root):


            if root == None:
                return

            #left
            inorder(root.left)

            #parent
            result.append(root.val)

            #right
            inorder(root.right)

        inorder(root)
        return result
        