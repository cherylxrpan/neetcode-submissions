class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        stack = []
        output = 0

        for p, s in pair:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                output += 1
        
        return len(pair) - output

