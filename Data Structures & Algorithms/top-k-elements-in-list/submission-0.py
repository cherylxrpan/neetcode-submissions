class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = {}
        for key in nums:
            if key not in output:
                output[key] = 0
            output[key] += 1
        return sorted(output, key = output.get, reverse = True)[:k]