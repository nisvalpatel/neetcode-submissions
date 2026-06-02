# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            if root == None:
                return 0

            left_ = height(root.left)
            right_ = height(root.right)

            if right_ == -1 or left_ == -1 or abs(left_ - right_) > 1:
                return -1
            
            return max(left_, right_) + 1

        
        temp = height(root)

        if temp == -1:
            return False

        return True