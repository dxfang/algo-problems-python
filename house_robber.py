class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        previous = 0
        current = 0
        
        for num in nums:
            old_previous = previous
            previous = current
            current = max(old_previous + num, previous)
            
        return current