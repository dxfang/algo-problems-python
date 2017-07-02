class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        
        # Using a set instead of a list in order to avoid TLE
        sq = set()
        
        i = 0
        
        while i*i <= c:
            sq.add(i*i)
            i += 1
            
        for j in sq:
            if c - j in sq:
                return True
                
        return False