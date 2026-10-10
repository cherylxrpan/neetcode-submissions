class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        res = 0
        l = 0
        r = len(heights) - 1

        while l<r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        
        return res
# You can't sort heights first. Compare with 3Sum and Two Sum II: there, sorting was fine because you only cared about values. The answer was the numbers themselves, not where they sat. Here the answer depends on positions, so sorting destroys information you need.