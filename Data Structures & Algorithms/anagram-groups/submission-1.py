class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key not in output:
                output[key] = []
            output[key].append(str)
        return list(output.values())