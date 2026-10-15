class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        # not possible to split into this many sized groups
        if len(hand) % groupSize != 0:
            return False

        #lets make the hash table
        hashTable = defaultdict(int)
        for num in hand:
            hashTable[num] += 1

        sorted_vals = sorted(hand)

        for val in sorted_vals:
            if hashTable[val] == 0:
                continue
            hashTable[val] -= 1
            for i in range(1, groupSize):
                
                if hashTable[val + i] == 0:
                    return False
                
                hashTable[val + i] -= 1
        
        return True

