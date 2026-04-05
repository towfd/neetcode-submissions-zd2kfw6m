class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # burte solution
        # using hashmap to record total count of all elements
        # following k, choose the maximun number
        # time complexity, hashmap take O(n) time, choose the maximun
        # number take O(n^k), total complexity is O(n + n^k)
        # space complexity, O(n) 
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

