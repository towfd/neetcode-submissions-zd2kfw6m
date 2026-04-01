class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Approach: Two-Pass Hash Table
        # Pass 1: Build a hash map mapping each element's value to its index.
        # Pass 2: Iterate through the array to check if the complement (target - num) exists in the hash map.
        # Ensure the complement is not the current element itself to avoid reusing the same index.
        # Time Complexity: O(N). We traverse the list containing N elements exactly twice.
        # Space Complexity: O(N). The hash map stores at most N key-value pairs.
        hashmap = {}
        for i, num in enumerate(nums):
            hashmap[num] = i

        for i, num in enumerate(nums):
            difference = target - num
            if (difference in hashmap) and (i != hashmap[difference]):
                if i < hashmap[difference]:
                    return [i, hashmap[difference]]
                else:
                    return [hashmap[difference], i]