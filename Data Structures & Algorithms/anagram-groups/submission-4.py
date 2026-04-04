class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # naive Solution using Hash Map
        # We use a hash map (str_hash_map) to group anagrams together. 
        # The key is the sorted version of the string, and the value is a list of the original strings.
        
        # Time Complexity: O(n * m log m), where 'n' is the total number of strings in 'strs', 
        # and 'm' is the maximum length of a string. Sorting each string takes O(m log m) time.
        # Space Complexity: O(n * m), as we store all 'n' strings of maximum length 'm' inside the hash map.
        str_hash_map = {}
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str in str_hash_map:
                str_hash_map[sorted_str].append(str)
            else:
                str_hash_map[sorted_str] = [str]
        return list(str_hash_map.values())