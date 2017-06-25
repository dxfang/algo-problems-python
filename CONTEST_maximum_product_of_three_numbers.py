class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Sort the list
        nums.sort()
        
        """
        Compare two cases:
        1. the product of the three largest positivenumbers in the list
        2. the product of the largest positive number and the two smallest negative numbers in the list
        """
        return max(nums[-1]*nums[-2]*nums[-3], nums[-1]*nums[0]*nums[1])