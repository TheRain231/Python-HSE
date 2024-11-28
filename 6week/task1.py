"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/description
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        left = 0
        maxLen = 0
        visited = {}

        for right in range(len(s)):
            if s[right] in visited and visited[s[right]] >= left:
                left = visited[s[right]] + 1

            visited[s[right]] = right
            maxLen = max(maxLen, right - left + 1)

        return maxLen
