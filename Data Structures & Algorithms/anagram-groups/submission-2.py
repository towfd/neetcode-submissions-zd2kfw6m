class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_hash_map = {}
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str in str_hash_map:
                str_hash_map[sorted_str].append(str)
            else:
                str_hash_map[sorted_str] = [str]
        return [result_list for result_list in str_hash_map.values()]