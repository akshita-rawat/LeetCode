class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Map to store the most recent index of each character
        char_map = {}
        left = 0
        max_length = 0
        
        for right, char in enumerate(s):
            # If the character is repeated and within the current window, move the left pointer
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            
            # Update the character's last seen position
            char_map[char] = right
            # Calculate the current window size and update max_length
            max_length = max(max_length, right - left + 1)
            
        return max_length
