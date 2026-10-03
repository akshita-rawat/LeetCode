class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        
        while left < right:
            # The height of the container is limited by the shorter line
            current_height = min(height[left], height[right])
            # The width is the distance between the two pointers
            width = right - left
            # Calculate the area and update max_water if it's larger
            max_water = max(max_water, current_height * width)
            
            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water
