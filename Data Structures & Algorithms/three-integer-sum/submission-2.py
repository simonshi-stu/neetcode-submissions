class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # result = set()
        # n = len(nums)
        # for i in range(n - 2):
        #     seen = set()
        #     for j in range(i + 1, n):
        #         compliment = -(nums[i] + nums[j])
        #         if compliment in seen:
        #             output = tuple(sorted([nums[i], nums[j], compliment]))
        #             result.add(output)
        #         seen.add(nums[j])
        # return [list(i) for i in result]
        nums.sort()
        result = set()
        n = len(nums)
        if n < 3:
            return []
        if nums[0] > 0 or nums[-1] < 0:
            return []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            seen = set()
            for j in range(i + 1, n):
                compliment = -(nums[i] + nums[j])
                if compliment in seen:
                    result.add((nums[i], compliment, nums[j]))
                seen.add(nums[j])
        return [list(triplet) for triplet in result]
