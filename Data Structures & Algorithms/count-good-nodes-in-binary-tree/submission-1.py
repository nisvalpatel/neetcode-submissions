# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(max_val, node):
            nonlocal count
            if node == None:
                return
            
            if node.val >= max_val:
                count += 1
            
            dfs(max(max_val, node.val), node.left)
            dfs(max(max_val, node.val), node.right)

        
        dfs(-101, root)

        return count