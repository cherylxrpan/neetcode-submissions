class Solution:
    def binarysearch(self, l: int, r: int, nums: List[int], target: int) -> int:
        if l>r:
            return -1

        m = l + (r-l)//2

        if target == nums[m]:
            return m
        elif target > nums[m]:
            return self.binarysearch(m+1, r, nums, target)
        elif target < nums[m]:
            return self.binarysearch(l, m-1, nums, target)
        else:
            return -1
    def search(self, nums: List[int], target: int) -> int:
        return self.binarysearch(0, len(nums)-1, nums, target)

        