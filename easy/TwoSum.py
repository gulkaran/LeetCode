# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        
        for i in range(len(nums)):
            
            if (target-nums[i]) in hashmap:
                return [hashmap.get(target-nums[i]), i]
            
            hashmap.update({nums[i]: i})