class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        elif k > 0:
            return len(set(nums)&set(i+k for i in nums))
        else:
            duplicate = []
            count = 0
            for x in range(len(nums)):
                for y in range(x+1,len(nums)):
                    if nums[x] - nums[y] == 0 and nums[x] not in duplicate:
                        count += 1
                        duplicate.append(nums[x])
            return count