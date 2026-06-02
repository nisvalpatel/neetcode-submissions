class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
    
        visited = set()
        ret_list = []
        temp_list = []

        def rec():
            if len(visited) == len(nums):
                ret_list.append(temp_list.copy())
                return
            
            for i in range(len(nums)):
                if i in visited:
                    continue
                
                visited.add(i)
                temp_list.append(nums[i])
                rec()

                visited.remove(i)
                temp_list.pop()
            
        rec()
        return ret_list


        