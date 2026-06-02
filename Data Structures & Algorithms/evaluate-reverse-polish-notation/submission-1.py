class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tok in tokens:
            if tok == "-":
                first = stack.pop()
                second = stack.pop()
                tok = second - first

            elif tok == "+":
                first = stack.pop()
                second = stack.pop()
                tok = second + first

            elif tok == "*":
                first = stack.pop()
                second = stack.pop()
                tok = second * first

            elif tok == "/":
                first = stack.pop()
                second = stack.pop()
                tok = int(second / first
)
            stack.append(int(tok))
        
        return stack.pop()
