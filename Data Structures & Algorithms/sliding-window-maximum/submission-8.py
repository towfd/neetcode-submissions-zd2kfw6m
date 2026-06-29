class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 建立一個答案陣列
        # 建立一個max_heap, 每次有新的數進來的時候，將這個heap調整好，這樣每次在最上面的就會是最大值
        # 時間複雜度O(nlogn) -> logn為調整heap的時間
        # 空間複雜度O(n)

        target_list = []
        max_heap = []

        for idx in range(len(nums)):
            max_heap.append(idx)
            cur_idx = len(max_heap) - 1
            while cur_idx > 0:
                parent_idx = (cur_idx - 1) // 2
                if nums[max_heap[cur_idx]] > nums[max_heap[parent_idx]]:
                    max_heap[cur_idx], max_heap[parent_idx] = max_heap[parent_idx], max_heap[cur_idx]
                    cur_idx = parent_idx
                else:
                    break

            while max_heap and max_heap[0] < idx - k + 1:
                if len(max_heap) == 1:
                    max_heap.pop()
                else:
                    cur_d_idx = 0
                    max_heap[0] = max_heap.pop()
                    while True:
                        l_child_idx = cur_d_idx * 2 + 1
                        r_child_idx = cur_d_idx * 2 + 2
                        largets_idx = cur_d_idx
                        if l_child_idx < len(max_heap) and nums[max_heap[l_child_idx]] > nums[max_heap[largets_idx]]:
                            largets_idx = l_child_idx
                        
                        if r_child_idx < len(max_heap) and nums[max_heap[r_child_idx]] > nums[max_heap[largets_idx]]:
                            largets_idx = r_child_idx

                        if cur_d_idx == largets_idx:
                            break

                        max_heap[cur_d_idx], max_heap[largets_idx] = max_heap[largets_idx], max_heap[cur_d_idx]
                        cur_d_idx = largets_idx
            if idx >= k - 1:
                target_list.append(nums[max_heap[0]])
        return target_list   