class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Approach: One-Pass Hash Table
        # 1. Initialize an empty hash map to store numbers and their corresponding indices.
        # 2. Iterate through the array. For each element, calculate its complement (target - current number).
        # 3. Check if this complement already exists in the hash map.
        # 4. If it exists, we found the pair! Return the index of the complement and the current index.
        # 5. If it does not exist, add the current number and its index to the hash map for future lookups.
        # Note: Time complexity is O(N) and Space complexity is O(N).
        hashmap = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in hashmap:
                return [hashmap[difference], i]
            hashmap[num] = i