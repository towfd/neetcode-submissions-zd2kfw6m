class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort Approach (Optimal O(n) Solution)
        # First, count the frequency of each number using a hash map.
        # Second, create an array of lists (buckets) where the index represents the frequency.
        # Finally, iterate through the buckets from right to left (highest frequency to lowest) 
        # and collect the numbers until we reach k elements.
        
        # Time complexity: O(n), since we iterate through the list and the buckets a constant number of times.
        # Space complexity: O(n), to store the hash map and the bucket array.
        
        frequent_hashmap = {}
        result_list = []
        
        # 1. Count frequencies
        for num in nums:
            if num in frequent_hashmap:
                frequent_hashmap[num] += 1
            else:
                frequent_hashmap[num] = 1
                
        # 2. Create buckets where index = frequency
        frequent_bucket = [[] for _ in range(len(nums) + 1)]
        for key, value in frequent_hashmap.items():
            frequent_bucket[value].append(key)

        # 3. Gather the top k elements from the highest frequency buckets
        for bucket in reversed(frequent_bucket):
            for value in bucket:
                result_list.append(value)
                # Early return as soon as we collected k elements!
                if k == len(result_list):
                    return result_list
        
        return result_list