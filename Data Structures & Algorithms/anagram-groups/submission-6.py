class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_hash_map = {}
        for str in strs:
            char_list = [0] * 26
            for char in str:
                char_list[ord(char) - ord('a')] += 1
            if tuple(char_list) in str_hash_map:
                str_hash_map[tuple(char_list)].append(str)
            else:
                str_hash_map[tuple(char_list)] = [str]
        return list(str_hash_map.values())