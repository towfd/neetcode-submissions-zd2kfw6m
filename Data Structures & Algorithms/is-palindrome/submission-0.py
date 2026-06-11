class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 會將這個字串以正則表達式的方法 將除了英文以及數字的符號清除
        # 將此字串反轉並進行比對
        # 若反轉前跟反轉後的相同，則代表這個字串是符合我們要求的
        # 時間複雜度：清除的時間O(n) 反轉字串的時間 O(n) 比對的時間 O(1)
        # 故時間複雜度約 = O(2n)
        # 空間複雜度：因為要有一個多出來的陣列，故空間複雜度為O(n)
        import re
        pattern = re.compile(r'[A-Za-z0-9]+')
        matches = pattern.findall(s)
        result = "".join(matches)
        if result.lower() == result[::-1].lower():
            return True
        else:
            return False
