class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        element_count = dict() # element: count(element)
        
        for num in nums:
            element_count[num] = element_count.get(num, 0) + 1
            
        count_to_element = dict() # count element: list of elements
        
        for element, count in element_count.items():
            if count in count_to_element:
                count_to_element[count].append(element)
            else:
                count_to_element[count] = [element]
        
        result = list()
        for i in range(len(nums), 0, -1):
            if count_to_element.get(i, None) != None:
                result.extend(count_to_element[i])
            else:
                continue
            
            if len(result) == k:
                return result