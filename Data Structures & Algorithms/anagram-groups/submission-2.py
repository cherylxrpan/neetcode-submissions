class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for str in strs:
            count = [0]*26
            for c in str:
                count[ord(c) - ord('a')] += 1
            output[tuple(count)].append(str)
        return list(output.values())