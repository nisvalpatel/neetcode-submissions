class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1

        if n <= 1:
            return 1
        
        for i in range(2, n+ 1):
            temp = a + b
            b = a
            a = temp

        return a