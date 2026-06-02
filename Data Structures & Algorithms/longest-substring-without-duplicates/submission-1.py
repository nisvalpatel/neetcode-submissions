class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # I think the strategy is to do a sliding window such that 
        # it basically 

        if not s:
            return 0

        if len(s) == 1:
            return 1

        max_length = 0
        front, back = 0, 0
        temp_set = {s[0]}

        def increment_front(element, front, back):
            while s[front] != element:
                temp_set.remove(s[front])
                front += 1

            front += 1
            return front


        while back < len(s) -1:
            back += 1
            if s[back] in temp_set:
                front = increment_front(s[back], front, back)
            temp_set.add(s[back])
            if ((back - front) + 1) > max_length:
                max_length = (back - front) + 1

        return max_length

            

                    

            


