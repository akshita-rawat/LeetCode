class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Split the string by whitespace, which automatically removes extra spaces
        words = s.split()
        
        # If the string contains no words, return 0
        if not words:
            return 0
            
        # Return the length of the last word in the list
        return len(words[-1])
