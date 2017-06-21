class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Find the largest number n
        n = len(nums)
        
        # Subtract the sum of all numbers in nums ( sum(nums) ) from the sum of ( 1+2+...+n )
        return n * (n + 1) / 2 - sum(nums)