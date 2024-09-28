"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/decode-string/description
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur = []
        ans = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                n = i + 1
                while s[n].isdigit():
                    n += 1
                stack.append(int(s[i:n]))
                i = n
                cur.append(ans)
                ans = ""
            elif s[i] == "]":
                k = int(stack.pop())
                temp = ans
                ans = cur.pop()
                ans += k * temp
            else:
                ans += s[i]
            i += 1
        return ans
