class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        n = len(nums)
        for i in range(n - 2):
            seen = set()
            for j in range(i + 1, n):
                compliment = -(nums[i] + nums[j])
                if compliment in seen:
                    output = tuple(sorted([nums[i], nums[j], compliment]))
                    result.add(output)
                seen.add(nums[j])
        return [list(i) for i in result]

