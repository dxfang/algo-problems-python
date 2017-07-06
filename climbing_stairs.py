class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n < 3:
            return n
        
        '''
        Base Conditions
        '''
        two_steps_below = 1
        one_step_below = 2
        current_step = 0
        
        for i in range(2, n):
            # [n] = [n-1] + [n-2]
            current_step = one_step_below + two_steps_below
            # [n-1] is now [n-2], one step lower
            two_steps_below = one_step_below
            # [n] is now [n-1], one step lower
            one_step_below = current_step
            
        return current_step