class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        before_r = len(nums)
        before_c = len(nums[0])
        
        if before_r * before_c != r * c or before_r == r and before_c == c:
            return nums
        
        # Transform the matrix into a list
        single_list = [j for i in nums for j in i]
        
        # Transform the list into a new matrix with Row r and Column C
        matrix = [single_list[i:i+c] for i in range(0,len(single_list),c)]
        
        return matrix