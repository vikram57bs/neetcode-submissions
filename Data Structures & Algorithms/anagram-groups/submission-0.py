class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd=defaultdict(list)
        for i in strs:
            k="".join(sorted(i))
            dd[k].append(i)
        return list(dd.values())