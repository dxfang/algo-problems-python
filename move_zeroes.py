class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        """
        Original solution
        """

        # index = 0
        # tail = len(nums) - 1
        
        # while index < tail:
        #     if nums[index] == 0:
        #         nums.append(0)
        #         del nums[index]
        #         tail -= 1
        #     else:
        #         index += 1


        """
        A better performance solution
        """

        non_zero_index = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1
                
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0