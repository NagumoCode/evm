class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            elif token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif token == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))

        return stack[0]