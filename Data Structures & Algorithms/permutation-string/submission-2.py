class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        '''
        Okay to solve this problem, I will basically have a sliding window
        of size 26 (so basically size of alphabet). and basically do sliding
        window where I will do +1 in the corresponding index of the list to
        account for the s1 
        '''

        #edge case: s2 is smaller than s1
        if len(s2) < len(s1):
            return False

        alphabet = [0] * 26

        def check():
            for letter in alphabet:
                if letter != 0:
                    return False
            
            return True
        
        #setting the list up for s1
        for char in s1:
            alphabet[ord(char) - ord('a')] -= 1
        

        #setting up the list with the sliding window
        left = 0
        right = 0
        alphabet[ord(s2[right]) - ord('a')] += 1

        while right - left < len(s1) - 1:
            right += 1
            alphabet[ord(s2[right]) - ord('a')] += 1

        if check():
            return True

        while right < len(s2):
            alphabet[ord(s2[left]) - ord('a')] -= 1
            left += 1
            right += 1
            if right < len(s2):
                alphabet[ord(s2[right]) - ord('a')] += 1

            if check():
                return True
            


        return False




