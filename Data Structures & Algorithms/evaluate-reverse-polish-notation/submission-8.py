class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 暴力破解
        # 遞迴去找到運算符號
        # 當找到運算符號後，將運算符號前兩個數字做運算
        # 運算完畢後，運用切片的方式修改陣列
        # 時間複雜度O(N^2)
        # 空間複雜度O(N)
        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in ['+', '-', '*', '/']:
                    op = tokens[i]
                    num1 = int(tokens[i - 1])
                    num2 = int(tokens[i - 2])
                    if op == '+': result = num2 + num1
                    elif op == '-': result = num2 - num1
                    elif op == '*': result = num2 * num1
                    elif op == '/': result = int(num2 / num1)  
                    tokens = tokens[:i - 2] + [str(result)] + tokens[i + 1:]
                    
                    break
        result = int(tokens[0])
        return result