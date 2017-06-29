class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
            
        localsum = maxsum = nums[0]
        
        for num in nums[1:]:
            localsum = max(num, localsum + num)
            maxsum = max(localsum, maxsum)
            
        return maxsum