from typing import Dict, List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_to_origin: Dict[str, List[str]] = dict()
            
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in sorted_to_origin:
                sorted_to_origin[sorted_word] = [word]
            else:
                sorted_to_origin[sorted_word].append(word)
        
        return [result for _, result in sorted_to_origin.items()]