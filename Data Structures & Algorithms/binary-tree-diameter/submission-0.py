# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_length =0

        def maxHeight(root):
            nonlocal max_length
            if root == None:
                return 0

            left_height = maxHeight(root.left)
            right_height = maxHeight(root.right)
            max_length = max(max_length, abs(right_height + left_height))

            return max(left_height, right_height) + 1
        maxHeight(root)
        return max_length