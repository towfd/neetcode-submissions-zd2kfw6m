class Solution:
    def isValid(self, s: str) -> bool:
        # 暴力破解
        # 針對每個遞迴到的符號，去尋找是否有相對應的閉環，找到後將其移除
        # 若最後字串不為空 回傳False
        # 時間複雜度 O(N^2)
        # 空間複雜度 O(1)
        while '()' in s or '[]' in s or "{}" in s:
            s = s.replace('()', '')
            s = s.replace("{}",'')
            s = s.replace('[]','')
        return s == ""
