class NumArray(object):
    # O(n) Init
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        
        self.pts = nums
        
        for pt in range(1,len(nums)):
            self.pts[pt] += self.pts[pt-1]
        
    # O(1) Query
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
            
        return self.pts[j] - (self.pts[i-1] if i > 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)