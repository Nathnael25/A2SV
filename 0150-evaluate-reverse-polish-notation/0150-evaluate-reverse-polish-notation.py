class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for c in tokens:
            if c in ["+", "-", "*", "/"]:
                a = stack.pop()
                b = stack.pop()
                if c == "+":
                    stack.append(b + a)
                elif c == "-":
                    stack.append(b - a)
                elif c == "*":
                    stack.append(b * a)
                else:
                    # handle negative division
                    if a * b < 0 and b % a != 0:
                        stack.append(b // a + 1)
                    else:
                        stack.append(b // a)
            else:
                stack.append(int(c))
        return stack[0]
                
                
