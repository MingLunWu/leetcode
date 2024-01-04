from typing import Dict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_counts:Dict[str, int]  = dict() # char: count
            
        for char_s in s:
            char_counts[char_s] = char_counts.get(char_s, 0) + 1
            
        for char_t in t:
            char_counts[char_t] = char_counts.get(char_t, 0) - 1
            
        for key in char_counts:
            if char_counts[key] != 0:
                return False
        
        return True