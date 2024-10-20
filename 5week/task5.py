"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/word-break/description
"""


from functools import cache


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        @cache
        def solve(s):
            if len(s) == 0:
                return True
            for word in wordDict:
                if word == s[0 : len(word)]:
                    if solve(s[len(word) :]):
                        return True
            return False

        return solve(s)
