class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Base cases
        if n <= 2:
            return n
        
        # Track the number of ways for the previous two steps
        # first = ways to reach step 1, second = ways to reach step 2
        first, second = 1, 2
        
        # Iteratively calculate ways up to the n-th step
        for _ in range(3, n + 1):
            current = first + second
            first = second
            second = current
            
        return second
