class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        result = [1]
        
        for i in range(rowIndex):
            result = [x + y for x, y in zip(result + [0], [0] + result)]
            
        return result