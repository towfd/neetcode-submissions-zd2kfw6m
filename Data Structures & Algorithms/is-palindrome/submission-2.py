class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 要將空間複雜度降到O(1)的層級，這邊會需要用到指標
        # 想法是這樣，建立兩個指標，一個從最左邊過來，一個從最右邊過來
        # 結束的條件是左邊指標大於右邊指標，或是說指標目前的文字不匹配
        # 另外清除特殊符號的部分可以用.isalnum來判斷是否為數字或是英文字母
        # 時間複雜度為O(n)，因為只要指標跑一遍的時間
        # 空間複雜度為O(1)，只需要兩個指標的空間
        left_cur, right_cur = 0, len(s) - 1
        while left_cur < right_cur:
            if not s[left_cur].isalnum():
                left_cur += 1
                continue
            if not s[right_cur].isalnum():
                right_cur -= 1
                continue
            if s[left_cur].lower() != s[right_cur].lower():
                return False
            left_cur += 1
            right_cur -= 1
        return True


