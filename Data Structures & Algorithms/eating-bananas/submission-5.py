class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search
        # 給定兩個索引，去搜尋他的中間值，如果說中間值太小，右邊指標往左一點，太大，左邊指標往右一點
        # 直到兩個指標相會為止
        # 優化
        # 第一：如果陣列長度剛好與時間相等，直接返回h，因為一個小時只能吃一個pile
        # 第二：優化左邊界，算法為 總pile數 / 總時間
        # 時間複雜度O(nlogm) -> n 為pile的大小 logm 為找到hours的時間
        # 空間複雜度O(1)
        
        if len(piles) == h:
            return max(piles)

        l_idx = math.ceil(sum(piles) / h)
        r_idx = max(piles)
        while l_idx <= r_idx:
            speed = (l_idx + r_idx) // 2
            hours = 0
            for p in piles:
                hours += ((p + speed - 1) // speed)
            if hours <= h:
                r_idx = speed - 1
            else:
                l_idx = speed + 1
        return l_idx