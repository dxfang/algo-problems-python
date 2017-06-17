class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max = count = 0
        
        for i in nums:
            if i == 1:
                count += 1
            elif i == 0:
                if count > max:
                    max = count
                count = 0
        if count > max:
            max = count
            
        return max