class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        # Solution 1
        
        return (haystack.index(needle) if needle in haystack else -1)
        
        # Solution 2
        
        if len(haystack) == 0 and len(needle) == 0:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
            
        return -1
                