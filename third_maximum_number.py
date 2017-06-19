class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        current_max = nums[-1]
        counter = 1
        
        for i in range(len(nums)-1, 0, -1):
            if nums[i] - nums[i-1] > 0:
                current_max = nums[i-1]
                counter += 1
            
            if counter == 3:
                return current_max
                
        return nums[-1]