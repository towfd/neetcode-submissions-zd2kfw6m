class Solution:
    def isValid(self, s: str) -> bool:
        # stack解法
        # 準備一個stack，將s遇到右閉環前的符號都先塞進去
        # 遇到右閉環後，依序將stuck裡面的內容取出，如果配對失敗，回傳False
        # 時間複雜度O(N)
        # 空間複雜度O(N)
        s_stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        ans = True
        for char in s:
            if char in mapping:
                top_ele = s_stack.pop() if s_stack else '#'
                if mapping[char] != top_ele:
                    return False
            else:
                s_stack.append(char)
        return not s_stack