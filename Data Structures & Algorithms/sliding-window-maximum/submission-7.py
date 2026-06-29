class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 建立一個答案陣列
        # 建立一個雙向陣列
        # 陣列規則為此，每次有新的數字進來，與前方數字對比，若較小，那就將前方數字踢出陣列，直到前方數字較大為止
        # 最前方的數字若超出index, 移除，由後方數字遞補
        # 時間複雜度O(n)
        # 空間複雜度O(n)

        target_list = []
        d_que = deque()
        for r_idx in range(len(nums)):
            if d_que and d_que[0] < (r_idx - k + 1):
                d_que.popleft()

            while d_que and nums[d_que[-1]] < nums[r_idx]:
                d_que.pop()

            d_que.append(r_idx)

            if r_idx >= k - 1:
                target_list.append(nums[d_que[0]])

        return target_list