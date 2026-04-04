class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Solve this problem with brute solution
        # we can iterate the list, and for each word we can check if all word is equal
        # First, we check the length of strs[i].length, if == 0, return [[""]]
        # Second we check the word which length is equal to the current word
        # Third we check the word if is equal, if not, continue, if right, add to the list
        # Finally return the list
        # Time complexity is O(n * m) which n is the list and m is the same length of the word 
        # Space complexity is O(n) which record the result

        result_list = []
        compared_str = []
        for str in strs:
            current_result_list = []
            str = sorted(str)
            if str in compared_str:
                continue
            for compare_str in strs:
                sorted_str = sorted(compare_str).copy()
                if str == sorted_str:
                    current_result_list.append(compare_str)
            compared_str.append(str)
            result_list.append(current_result_list)
        return result_list