class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_to_idx = dict() # value: idx
        
        for idx, num in enumerate(nums):
            desired_value = (target-num)
            if desired_value in value_to_idx:
                return [idx, value_to_idx[desired_value]]
            else:
                value_to_idx[num] = idx