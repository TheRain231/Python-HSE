"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/description
"""


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        i = 0
        curIndex = 0
        count = 0
        ans = 0
        while i < len(word):
            if word[i] == vowels[curIndex]:
                count += 1
            elif (
                i > 0
                and word[i - 1] == vowels[curIndex]
                and curIndex < len(vowels) - 1
                and word[i] == vowels[curIndex + 1]
            ):
                curIndex += 1
                count += 1
            else:
                if curIndex == len(vowels) - 1:
                    ans = max(ans, count)
                curIndex = 0
                count = 0
                if word[i] == vowels[curIndex]:
                    count += 1
            i += 1

        if curIndex == len(vowels) - 1:
            ans = max(ans, count)

        return ans
