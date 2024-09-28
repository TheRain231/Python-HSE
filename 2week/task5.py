"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/string-compression/description
"""


class Solution:
    def compress(self, chars: list[str]) -> int:
        last = chars[0]
        left = 0
        i = 1
        while i < len(chars):
            if chars[i] != last:
                last = chars[i]
                if i - left > 1:
                    chars[left + 1 : i] = str(i - left)
                    left += len(str(i - left))
                i = left
                left += 1
            i += 1
        if i - left > 1:
            chars[left + 1 : i] = str(i - left)
        return len(chars)
