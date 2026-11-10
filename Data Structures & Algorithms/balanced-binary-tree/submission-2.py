# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def rec(node):

            if node == None:
                return 1
            
            left = rec(node.left)
            right = rec(node.right)

            if left == -1 or right == -1 or abs(right - left) > 1:
                return -1
            
            return max(left, right) + 1
        
        ret = rec(root)

        if ret == -1:
            return False
        else:
            return True