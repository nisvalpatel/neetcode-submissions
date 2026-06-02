class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Given an array of ints that represent temperatures that 
        # represent the daily temperature on the ith day. I can use 
        # a stack to complete this problem. The stack will have the
        # index (not the value) of any problem that did not have a 
        n = len(temperatures)
        Output = [0] * n
        stack = []

        for i in range(n):
            if len(stack) == 0:
                stack.append(i)
                continue
            while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                temp = stack[-1]
                Output[temp] = i - temp
                stack.pop()
            stack.append(i)
        return Output
        


        