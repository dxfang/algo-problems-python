class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        
        temp_min = arrays[0][0]
        temp_max = arrays[0][-1]
        max_distance = 0
        
        for i in range(1,len(arrays)):
            max_distance = max(max_distance, abs(temp_min - arrays[i][-1]), abs(temp_max - arrays[i][0]))
            temp_min = min(temp_min, arrays[i][0])
            temp_max = max(temp_max, arrays[i][-1])
            
        return max_distance