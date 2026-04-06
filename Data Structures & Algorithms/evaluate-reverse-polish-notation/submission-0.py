class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token.isnumeric() or token[1:].isnumeric():
                st.append(int(token))
            else:
                op1 = st.pop()
                op2 = st.pop()
                res = 0
                match token:
                    case "+":
                        res = op1 + op2
                    case "-":
                        res = op2 - op1
                    case "*":
                        res = op1 * op2
                    case "/":
                        res = op2 // op1
                st.append(res)

        return st[-1]
