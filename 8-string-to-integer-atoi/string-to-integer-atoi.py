class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # 1. Ignore leading whitespace
        s = s.lstrip()
        if not s:
            return 0
        
        # 2. Check signedness
        sign = 1
        i = 0
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        # 3. Convert digits and handle clamp constraints
        res = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            
            # Overflow / Underflow check prior to addition
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN
                
            res = res * 10 + digit
            i += 1
            
        return sign * res
