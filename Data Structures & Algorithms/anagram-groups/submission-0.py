class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for str in strs:
            sortedS = ''.join(sorted(str))
            output[sortedS].append(str)
        return list(output.values())