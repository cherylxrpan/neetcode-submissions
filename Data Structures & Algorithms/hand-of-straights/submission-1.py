class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        for x in sorted(count):      
            need = count[x]                        # every remaining x starts a group
            if need:
                for v in range(x, x + groupSize):
                    if count[v] < need:
                        return False               # not enough of v to finish those groups
                    count[v] -= need
                    
        return True
        