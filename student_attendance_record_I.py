class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        return not ('LLL' in s or s.count('A') > 1)