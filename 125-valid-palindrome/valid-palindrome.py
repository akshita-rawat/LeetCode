class Solution(object):
    def isPalindrome(self, s):
        # Filter out non-alphanumeric characters and convert to lowercase
        filtered_s = "".join(char.lower() for char in s if char.isalnum())
        # Check if the string reads the same forwards and backwards
        return filtered_s == filtered_s[::-1]
