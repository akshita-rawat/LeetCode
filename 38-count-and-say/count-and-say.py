class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        current_string = "1"
        
        # Generate terms from 2 to n
        for _ in range(n - 1):
            next_string = []
            i = 0
            
            # Read through the current string to perform RLE
            while i < len(current_string):
                count = 1
                # Count consecutive identical characters
                while i + 1 < len(current_string) and current_string[i] == current_string[i + 1]:
                    count += 1
                    i += 1
                
                # Append the count followed by the digit character
                next_string.append(str(count) + current_string[i])
                i += 1
            
            current_string = "".join(next_string)
            
        return current_string
