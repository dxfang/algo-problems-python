class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        """
        Solution 1: Rotate the list by 1 by k times
        """

        itr = k % len(nums)
        
        for i in range(itr):
            nums.insert(0, nums[-1])
            nums.pop()

        """
        Solution 2: Reform the list using slice operations
        """

        itr = len(nums) - k % len(nums)        
        nums[:] = nums[itr:] + nums[:itr]