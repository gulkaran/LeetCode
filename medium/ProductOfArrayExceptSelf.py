# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answer = [1]

        # [1, 2, 3, 4]

        # compute the prefix - 1, 1, 2, 6

        for i in range(len(nums)-1):
            prefix = answer[i]

            prefix *= nums[i]

            answer.append(prefix)

        # compute the suffix - 24, 12, 4, 1

        suffixes = [1]*len(nums) 
        for i in range(len(nums)-1, 0, -1):
            suffix = suffixes[i]

            suffix *= nums[i]
            suffixes[i-1] = suffix

            answer[i] *= suffixes[i]
            
        answer[0] *= suffixes[0]
        return answer