# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        past_elements = {}
        
        for i in nums:
            if i in past_elements:
                return True
            
            past_elements.update({i : 0})
                
        
        return False