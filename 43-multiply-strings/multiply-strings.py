class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If either number is "0", the product is "0"
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Array to store the result of multiplication.
        # The maximum possible length of the product is len(num1) + len(num2)
        res = [0] * (len(num1) + len(num2))
        
        # Reverse iterate through num1 and num2
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                # Convert characters to digits using ord()
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                
                # Positions in the result array
                p1, p2 = i + j, i + j + 1
                
                # Add multiplication result to the current position
                total = mul + res[p2]
                
                # Update positions with carry and remainder
                res[p2] = total % 10
                res[p1] += total // 10
        
        # Convert the digits array back to a string, skipping leading zeroes
        result_str = []
        for digit in res:
            if not (len(result_str) == 0 and digit == 0):
                result_str.append(str(digit))
                
        return "".join(result_str)
