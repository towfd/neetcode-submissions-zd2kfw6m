class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Sorting Approach
        # First, use a hash map to record the frequency of each element.
        # Second, turn the hash map into a list of tuples, then sort it by frequency in descending order.
        # Finally, slice the top k elements and return their keys.
        
        # Time Complexity: O(n log n), where n is the number of unique elements. 
        # Counting frequencies takes O(n), and sorting the elements takes O(n log n).
        # Space Complexity: O(n), to store the hash map and the list of tuples.
        frequent_hashmap = {}
        for num in nums:
            if num in frequent_hashmap:
                frequent_hashmap[num] += 1
            else:
                frequent_hashmap[num] = 1

        result_list = [(key, value) for key, value in frequent_hashmap.items()]
        result_list = sorted(result_list, key= lambda x: -x[1])
        result_list = [key for key, value in result_list[:k]]
        return result_list