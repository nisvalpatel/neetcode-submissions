class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        phoneDict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ret = []
        def dfs(string, index):
            if index >= len(digits):
                if string != "":
                    ret.append(string)
                return
            
            for char in phoneDict[digits[index]]:
                dfs(string + char, index + 1)
        

        dfs("", 0)

        return ret