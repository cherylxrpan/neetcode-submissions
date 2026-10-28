class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1                     # the last index trivially "reaches" itself
        for i in range(len(nums) - 2, -1, -1):   # from the second-to-last index back to 0
            if i + nums[i] >= goal:              # the farthest jump from i covers the goal?
               goal = i                         # then i works, and it's the new target
        
        return goal == 0                         # did the goal reach the start?