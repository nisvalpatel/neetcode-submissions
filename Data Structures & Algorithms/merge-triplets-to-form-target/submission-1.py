class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        

        temp = [0, 0, 0]

        for triplet in triplets:
            if triplet[0] == target[0]:
                if triplet[1] <= target[1] and triplet[2] <= target[2]:
                    temp = [max(temp[0], triplet[0]),max(temp[1], triplet[1]), max(temp[2], triplet[2])]
            elif triplet[1] == target[1]:
                if triplet[0] <= target[0] and triplet[2] <= target[2]:
                    temp = [max(temp[0], triplet[0]),max(temp[1], triplet[1]), max(temp[2], triplet[2])]
            elif triplet[2] == target[2]:
                if triplet[0] <= target[0] and triplet[1] <= target[1]:
                    temp = [max(temp[0], triplet[0]),max(temp[1], triplet[1]), max(temp[2], triplet[2])]
            
        
        if target[0] == temp[0] and target[1] == temp[1] and target[2] == temp[2]:
            return True

        return False