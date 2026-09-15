class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = dict()
        for i in nums:
            a[i] = a.get(i, 0) + 1
        sorted_item = sorted(a.items(), key = lambda x : x[1], reverse = True)
        return [i for i, count in sorted_item[:k]]
