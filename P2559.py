from typing import List


class Solution:
    def check(self, word: str) -> bool:
        return word[0] in ['a', 'e', 'i', 'o', 'u'] and word[-1] in ['a', 'e', 'i', 'o', 'u']

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        diff = [0]
        cnt = 0
        for word in words:
            if self.check(word):
                cnt = cnt + 1
            diff.append(cnt)
        result = []
        for query in queries:
            result.append(diff[query[1] + 1] - diff[query[0]])
        return result
