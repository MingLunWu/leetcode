class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for x in nums] # init with 1

        # forward (from 0 to len(nums)-1)
        forward_product = 1
        for idx in range(len(nums)):
            if idx == 0: # no prefix elements
                continue
            else:
                forward_product *= nums[idx-1]
                result[idx] = forward_product

        # backward (from len(nums)-1 to 0)
        backward_product = 1
        for idx in range(len(nums)-1, -1, -1):
            if idx == len(nums) -1 : # no backward elements
                continue
            else:
                backward_product *= nums[idx+1]
                result[idx] *= backward_product
        
        return result
            
            