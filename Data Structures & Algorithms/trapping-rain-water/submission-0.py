class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        ans = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if height[left] < height[right]:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1
        return ans