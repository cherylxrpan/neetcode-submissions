class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1                      # fact 1
        tank, start = 0, 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]       # diff[i]
            if tank < 0:       
                tank, start = 0, i + 1    
                
        return start              


# time: O(n)
# space: O(1)