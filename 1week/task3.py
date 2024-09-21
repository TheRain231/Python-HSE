"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        binArray = [0] * len(s)
        for i in range(len(s)):
            if s[i] == "(":
                stack.append((s[i], i))
            else:
                if len(stack) > 0 and stack[-1][0] == "(":
                    binArray[stack[-1][1]] = 1
                    binArray[i] = 1
                    stack.pop(-1)
                else:
                    stack.append((s[i], i))
        ans = 0
        cur = 0
        for i in binArray:
            if i == 1:
                cur += 1
                ans = max(ans, cur)
            else:
                cur = 0
        return ans
