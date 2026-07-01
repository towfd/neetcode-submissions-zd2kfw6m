import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 建立一個運算的map
        # 建立一個stack，遇到數字塞入，遇到符號，取出兩個數字，根據符號去運算
        # 時間複雜度 O(n)
        # 空間複雜度 O(n)
        ope_map = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b)
        }
        num_stack = []
        for t in tokens:
            if t not in ope_map:
                num_stack.append(int(t))
            else:
                s1 = num_stack.pop()
                s2 = num_stack.pop()
                ope_ans = ope_map[t](s2, s1)
                num_stack.append(ope_ans)
        return num_stack.pop()