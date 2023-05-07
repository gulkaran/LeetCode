# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # if length of nums is 1
        if len(nums) == 1:
            return nums[0]

        # max sum, total, left/right pointers
        max_sum = nums[0]
        total = 0

        for i in range(len(nums)): # [-2, 1, -3, 4, -1, 2, 1, -5, 4]

            if total < 0:
                total = 0
            
            total += nums[i]
            
            # keep track of the largest total
            if total > max_sum:
                max_sum = total

        return max_sum