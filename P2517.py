from math import inf
from typing import List


class Solution:
    def check(self, price: List[int], k: int, m: int):
        prev = -inf
        cnt = 0
        for p in price:
            if (p - prev) >= m:
                cnt = cnt + 1
                prev = p
        return cnt >= k

    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        l = 0
        r = price[-1] - price[0] + 1
        while l < r:
            m = (l + r) // 2
            if self.check(price, k, m):
                l = m + 1
            else:
                r = m
        return l - 1
