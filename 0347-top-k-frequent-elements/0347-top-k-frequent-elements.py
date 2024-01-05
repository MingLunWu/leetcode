class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        element_count = dict()
        
        for num in nums:
            element_count[num] = element_count.get(num, 0) + 1
            
        sorted_dict = sorted(element_count.items(), key=lambda x: x[1], reverse=True)
        
        return [x[0] for x in sorted_dict[:k]]