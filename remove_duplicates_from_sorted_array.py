class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) <= 1:
            return len(nums)
        
        index = 0
        current = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] != current:
                current = nums[i]
                index += 1
                nums[index] = current
            
        nums[:] = nums[:index + 1]
        
        return len(nums)