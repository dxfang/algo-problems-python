class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        # Create a dictionary to store the values and their indices in nums
        dict = {}
        
        for index, num in enumerate(nums):
            if num in dict and index - dict[num] <= k:
                return True
            dict[num] = index
            
        return False