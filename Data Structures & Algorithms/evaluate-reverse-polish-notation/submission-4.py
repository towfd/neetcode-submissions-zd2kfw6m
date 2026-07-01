class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 建立一個stack，遇到數字塞入，遇到符號，取出兩個數字，根據符號去運算
        # 時間複雜度 O(n)
        # 空間複雜度 O(n)

        num_stack = []
        for t in tokens:
            if t not in ['+', '-', '*', '/']:
                num_stack.append(int(t))
            else:
                s1 = num_stack.pop()
                s2 = num_stack.pop()
                if t == '+':
                    num_stack.append(s2 + s1)
                elif t == '-':
                    num_stack.append(s2 - s1)
                elif t == '*':
                    num_stack.append(s2 * s1)
                elif t == '/':
                    num_stack.append(int(s2 / s1))
                else:
                    return 0
        return num_stack.pop()