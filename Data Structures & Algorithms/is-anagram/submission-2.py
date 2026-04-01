class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # brute
        if len(s) != len(t):
            return False
        s_count_map = {}
        for i in s:
            if i not in s_count_map:
                s_count_map[i] = 1
            else:
                s_count_map[i] += 1

        t_count_map = {}
        for i in t:
            if i not in s_count_map:
                return False

            if i not in t_count_map:
                t_count_map[i] = 1
            else:
                t_count_map[i] += 1
        for k, v in t_count_map.items():
            if t_count_map[k] != s_count_map[k]:
                return False
        return True