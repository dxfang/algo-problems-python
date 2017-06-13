class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        
        if len(flowerbed) == 1:
            if flowerbed[0] == 1:
                return False
            else:
                return True
        
        for i in range(len(flowerbed)):
            if n > 0:
                if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                elif i == len(flowerbed) - 1 and flowerbed[i-1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    n -= 1
                elif flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            else:
                return True
        
        if n > 0:            
            return False
        else:
            return True