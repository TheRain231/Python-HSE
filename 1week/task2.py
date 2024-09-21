"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLenght = 0
        left = 0
        nonRepeated = set()

        for right in range(len(s)):
            if s[right] not in nonRepeated:
                nonRepeated.add(s[right])
                maxLenght = max(maxLenght, right - left + 1)
            else:
                while s[right] in nonRepeated:
                    nonRepeated.remove(s[left])
                    left += 1
                nonRepeated.add(s[right])
        return maxLenght
