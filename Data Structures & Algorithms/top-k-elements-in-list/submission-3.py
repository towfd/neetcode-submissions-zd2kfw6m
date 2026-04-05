class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute-force solution
        # First, use a hash map to record the frequency of each element.
        # Second, iterate k times. In each iteration, scan the hash map to find the 
        # current maximum frequency element that hasn't been chosen yet.
        
        # Time Complexity: O(k * n), where n is the number of unique elements. 
        # Counting frequencies takes O(n), and finding the max k times takes O(k * n).
        # Space Complexity: O(n), to store the hash map and the set of chosen numbers.
        frequent_hashmap = {}
        for num in nums:
            if num in frequent_hashmap:
                frequent_hashmap[num] += 1
            else:
                frequent_hashmap[num] = 1

        result_list = []
        choosed_number = 0
        choosed_num = set()
        while choosed_number != k:
            current_max_value = 0
            current_max = 0
            for key, value in frequent_hashmap.items():
                if key in choosed_num:
                    continue
                if current_max_value <= value:
                    current_max_value = value
                    current_max = key
            result_list.append(current_max)
            choosed_num.add(current_max)
            choosed_number += 1

        return result_list

