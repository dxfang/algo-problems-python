class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        # Prefix_Sums method solution
        sums = [0]
        # Create a list of sums such as [0, nums[0], nums[0] + nums[1], ... , nums[0] + nums[1] + ... + nums[n]]
        for i in nums:
            sums.append(sums[-1] + i)
        # The sum of k numbers is 0 + nums[0] + nums[1] + ... nums[k] - 0 = nums[0] + nums[1] + ... nums[k]
        max_sum = sums[k] - sums[0]
        # Find the max of all these sums in this for-loop
        for i in range(1, len(nums) - k + 1):
            if max_sum < sums[i+k] - sums[i]:
                max_sum = sums[i+k] - sums[i]
        # Find the average by the max sum
        return max_sum / float(k)