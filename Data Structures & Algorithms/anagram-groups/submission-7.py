class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Optimal Solution using Character Count (Frequency Array)
        # Instead of sorting, we use an array of size 26 to count the frequency of each letter.
        # This reduces the time complexity from O(n * m log m) to O(n * m).
        
        # Time Complexity: O(n * m), where 'n' is the number of strings and 'm' is the max string length.
        # Space Complexity: O(n * m), as we store all 'n' strings of maximum length 'm' inside the hash map.
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