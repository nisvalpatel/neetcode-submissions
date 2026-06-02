class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {"(": ")", "[": "]", "{": "}"}
        
        #I plan on using a stack where I will push any left parenthesis while
        #popping when there is a right parenthesis. I will use a dictionary
        # where if the value is in the key, I push while if the values are in
        # a value, I will pop.

        temp = []
        for char in s:
            if char in dictionary.keys():
                temp.append(char)
            else:
                if len(temp) == 0:
                    return False
                val = temp.pop()
                if char !=  dictionary[val]:
                    return False
        if len(temp) == 0:
            return True
        else:
            return False