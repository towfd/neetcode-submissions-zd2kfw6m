class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we can use set and check the length, because set don't allow duplicate
        # time complexity is O(n) since it need to transfer to set
        # space complexity also is O(n) because it need space for set
        # return len(set(nums)) != len(nums)

        # hash map
        duplicate_set = set()
        for i in nums:
            if i in duplicate_set:
                return True
            else:
                duplicate_set.add(i)
        return False