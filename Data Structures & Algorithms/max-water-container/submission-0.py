class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute Force
        max_water = 0

        for l in range(len(heights)):
            for r in range(l + 1, len(heights)):
                width = r - l
                min_height = min(heights[l], heights[r])
                water = width * min_height
                max_water = max(max_water, water)

        return max_water

