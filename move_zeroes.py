class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        index = 0
        tail = len(nums) - 1
        
        while index < tail:
            if nums[index] == 0:
                nums.append(0)
                del nums[index]
                tail -= 1
            else:
                index += 1