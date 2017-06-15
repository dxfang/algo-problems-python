class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Sort the list
        sorted_nums = sorted(nums)
        
        result = 0
        
        # The minimums would be all the values in the sorted list with odd-number indices
        for i in range(0, len(nums), 2):
            result += sorted_nums[i]
            
        return result