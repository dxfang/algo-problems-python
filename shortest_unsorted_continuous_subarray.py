class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Create a sorted copy of the original array
        sorted_nums = sorted(nums)
        
        # Compare the left sides of both arrays to find out the beginning of the subarray
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                left_end = i
                # Compare the right sides of both arrays to find out the end of the subarray
                for j in range(len(nums)):
                    if nums[-1-j] != sorted_nums[-1-j]:
                        right_end = len(nums) - 1 - j
                        return right_end - left_end + 1 #Return the length of the subarray
        
        return 0    # If the original array is sorted, return 0