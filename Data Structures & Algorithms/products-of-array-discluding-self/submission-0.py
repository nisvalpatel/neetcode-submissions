class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #pre-computer  and post

        pre_list = [0]*len(nums)
        post_list = [0]*len(nums)

        pre_product = 1
        post_product = 1
        length = len(nums) - 1

        for i in range(len(nums)):
            pre_list[i] = pre_product
            pre_product *= nums[i]

            post_list[length - i] = post_product
            post_product *= nums[length - i]

        ret_list = []

        for i in range(len(nums)):
            ret_list.append(pre_list[i] * post_list[i])
        
        return ret_list


