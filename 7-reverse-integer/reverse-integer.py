class Solution(object):
    def reverse(self, x):
        # 32-bit signed integer boundaries
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        
        # Store the sign and work with the absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        res = 0
        while x != 0:
            digit = x % 10
            res = res * 10 + digit
            x //= 10
            
        # Re-apply the original sign
        res *= sign
        
        # Return 0 if the reversed integer overflows 32-bit limits
        if res < INT_MIN or res > INT_MAX:
            return 0
            
        return res
