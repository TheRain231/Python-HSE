"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-repeating-character-replacement/description
"""
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)
        res = 0
        i = 0

        for j in range(len(s)):
            letterJ = s[j]
            freqs[letterJ] += 1

            maxFreq = max(freqs.values())
            curLen = j - i + 1
            if curLen - maxFreq > k:
                freqs[s[i]] -= 1
                i += 1
                curLen = j - i + 1

            res = max(res, curLen)

        return res
