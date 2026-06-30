# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #let consider, left of root as one tree, and right of root as one tree.
        def symmetric(x,y):
            #this func check if 2 trees are summetric
            if x==None and y==None:
                return True
            if (x==None and y!=None) or (x!=None and y==None):
                return False
            if x.val != y.val:
                return False
            status_left = symmetric(x.left,y.right)
            status_right = symmetric(x.right,y.left)

            status = status_left and status_right

            return status
            
        if root == None:
            return True
            #since from the given original tree, the root node will be same even in the mirror image, we are taking left branch and right branch seperatly
        left_tree = root.left
        right_tree = root.right

        if symmetric(left_tree,right_tree):
            return True
        else:
            return False
                    


        