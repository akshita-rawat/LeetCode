class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        
        # Loop as long as there are digits to process or a carry remains
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
                
            # Append the remainder (0 or 1) to the result
            result.append(str(total % 2))
            # Calculate the new carry (0 or 1)
            carry = total // 2
            
        # The result is built backwards, so reverse it at the end
        return "".join(reversed(result))
