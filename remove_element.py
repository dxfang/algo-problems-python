class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        # if len(nums) == 0:
        #     return 0
            
        index = 0
        
        for i in range(len(nums)):
            if nums[i] == val:
                temp = nums[index]
                nums[index] = nums[i]
                nums[i] = temp
                index += 1
        
        nums[:] = nums[index:]
        
        return len(nums)