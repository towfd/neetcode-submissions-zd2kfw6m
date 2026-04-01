class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hash map
        # iterate the nums list, let difference = target - current num
        # if difference is in hash map
        # return the current num's index and the defference index
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