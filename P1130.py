from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return 0
        result = 0
        s = []
        for x in arr:
            while s and s[-1] <= x:
                y = s.pop()
                if not s or s[-1] >= x:
                    result = result + x * y
                else:
                    result = result + y * s[-1]
            s.append(x)
        while len(s) > 1:
            x = s.pop()
            result = result + x * s[-1]
        return result
