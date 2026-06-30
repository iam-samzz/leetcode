# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self,root: Optional[TreeNode],targetSum: int) -> bool:
        

        def path_sum(root,curr_sum):
            if root == None:
                return False
            
            curr_sum = curr_sum + root.val

            if (curr_sum == targetSum) and (root.left==None) and (root.right==None):
                return True

            status_left = path_sum(root.left,curr_sum)
            status_right = path_sum(root.right,curr_sum)

            status = status_left or status_right

            return status
        return path_sum(root,0)
        