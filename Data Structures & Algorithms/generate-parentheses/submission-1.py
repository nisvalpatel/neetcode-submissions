class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        

        ret = []

        def dfs(curr, count, diff):

            if n <= count and diff == 0:
                ret.append(curr)

            #adding left bracket "("
            if count < n:
                temp = curr + "("
                dfs(temp ,count + 1, diff + 1)


            #adding right bracket ")"
            if diff != 0:
                temp = curr + ")"
                dfs(temp, count, diff - 1)
                
            
        dfs("", 0, 0)
        return ret