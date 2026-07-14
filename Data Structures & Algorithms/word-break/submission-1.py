class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        '''
        I will try solving this problem by basically first solving
        the problem by basically solving it recursively and then
        I could add a hashing mechanism to basically make it dynamic
        programming.
        '''



        lst = [0] * len(s)

        def dfs(string):
            if len(string) > len(s):
                return False

            if string != s[:len(string)]:
                return False
            
            if len(string) == len(s):
                return True
            
            if lst[len(string) - 1] != 0:
                if lst[len(string) - 1] == -1:
                    return False
                if lst[len(string) - 1] != 1:
                    return True


            for word in wordDict:
                if dfs(string + word):
                    lst[len(string) - 1] = 1
                    return True
            
            lst[len(string) - 1] = -1
            return False

        
        return dfs("")

