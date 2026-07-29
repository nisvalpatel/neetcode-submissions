class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        temp = []
        def dfs(cur_index):
            if cur_index >= len(nums):
                ret.append(temp.copy())
                return
            
            dfs(cur_index + 1)
            temp.append(nums[cur_index])
            dfs(cur_index + 1)
            temp.pop()


        
        dfs(0)
        return ret