# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        count = 0
        answer = -1

        def dfs(root):
            nonlocal count
            nonlocal answer

            if root == None:
                return
            
            #going to leftmost branch (inorder traversal)
            dfs(root.left)
            
            #accounting for counting the root after left subtree complete
            count += 1

            if count == k:
                answer = root.val
            
            dfs(root.right)
        

        dfs(root)
        return answer
                


