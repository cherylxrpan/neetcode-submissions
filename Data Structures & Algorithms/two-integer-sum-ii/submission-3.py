class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) - 1
        while index1 < index2:
            s = numbers[index1] + numbers[index2]
            if s == target:
                return [index1 + 1, index2 + 1]
            elif s<target:
                index1 += 1
            else:
                index2 -=1
        return []
# it is one-indexed
# time complexity: O(n)
# space complexity: O(1)