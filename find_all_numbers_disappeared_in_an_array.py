class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        for num in nums:
            nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
            
        result = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
                
        return result