class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for x in nums] # init with 1
        postfix = [1 for x in nums] # init with 1
        
        end_idx = len(nums) - 1
        
        product = 1
        
        for idx in range(len(nums)):
            if idx == 0 :
                continue # keep 1
            else:
                product *= nums[idx-1]
                prefix[idx] = product
                
        product =1 
        
        for idx in range(-1, -1*(len(nums))-1, -1):
            if idx == -1:
                continue # keep 1
            else:
                product *= nums[idx+1]
                postfix[idx] = product
        
        result = list()
        for idx in range(len(nums)):
            result.append(prefix[idx] * postfix[idx])
            
        return result
            
            
            