class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_hashmap = {}
        result_list = []
        for num in nums:
            if num in frequent_hashmap:
                frequent_hashmap[num] += 1
            else:
                frequent_hashmap[num] = 1
        frequent_bucket = {i : -1 for i in range(len(nums) + 1)}
        for key, value in frequent_hashmap.items():
            if frequent_bucket[value] == -1:
                frequent_bucket[value] = [key]
            else:
                frequent_bucket[value].append(key)

        for key, value in reversed(frequent_bucket.items()):
            if value == -1:
                continue

            result_list.extend(value)
            if len(result_list) == k:
                break

        return result_list