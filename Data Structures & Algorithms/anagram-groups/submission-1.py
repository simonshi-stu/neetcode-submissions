class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)
        for i in strs:
            sortedS = ''.join(sorted(i))
            a[sortedS].append(i)
        return list(a.values())