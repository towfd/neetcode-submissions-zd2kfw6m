class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute-force solution
        # First, use a hash map to record the frequency of each element.
        # Second, turn hashmap into list[tuple], then sort the result
        # Finally, slicing k element and return
        
        # Time Complexity: O(nlogn), where n is the number of unique elements. 
        # Counting frequencies takes O(n), and sort the element takes O(nlogn).
        # Space Complexity: O(n), to store the hash map and the set of chosen numbers.
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