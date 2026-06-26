class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 建立兩個hashmap，一個s 一個t 計算他們裡面的字母
        # 建立兩個指針，左指針先走到s裡面有t裡面字符的
        # 後續右指針從左指針開始走，直到走完，若全部字符都有，Return當前window內字串
        # 若結束了還是沒有，回傳""
        # 時間複雜度 O(n)
        # 空間複雜度 O(m)
        if len(s) < len(t):
            return ""
        t_hashmap = {}
        s_hashmap = {}
        archieve = 0
        min_archi = float('inf')
        lindex = 0
        ll, rl = 0, 0
        for i in t:
            t_hashmap[i] = t_hashmap.get(i, 0) + 1

        for rindex in range(len(s)):
            word = s[rindex]
            s_hashmap[word] = s_hashmap.get(word, 0) + 1
            if word in t_hashmap and t_hashmap[word] == s_hashmap[word]:
                archieve += 1
            while archieve == len(t_hashmap.keys()):
                archi = rindex - lindex + 1
                if min_archi > archi:
                    min_archi = archi
                    ll = lindex
                    rl = rindex
                lword = s[lindex]
                s_hashmap[lword] -= 1 
                if lword in t_hashmap and s_hashmap[lword] < t_hashmap[lword]:
                    archieve -= 1
                lindex += 1
        if min_archi != float('inf'):
            return s[ll: rl + 1]
        else:
            return ""
