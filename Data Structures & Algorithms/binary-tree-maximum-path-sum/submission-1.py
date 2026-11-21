# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        

        curr = root
        if not root:
            return None

        max_sum = root.val
        
        def dfs(curr):
            nonlocal max_sum
            if curr.right == None and curr.left == None:
                max_sum = max(curr.val, max_sum)
                return curr.val

            if curr.right:
                right = max(0, dfs(curr.right))
            else:
                right = 0
            
            if curr.left:
                left = max(0, dfs(curr.left))
            else:
                left = 0
            
            max_sum = max(max_sum, curr.val + right + left)

            return curr.val + max(right, left)

        dfs(curr)
        return max_sum

