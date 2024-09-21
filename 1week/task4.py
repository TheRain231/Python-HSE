"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/multiply-strings/description/
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        num = "0123456789"
        res = ""
        for x in s:
            if x == " " and len(res) == 0:
                continue
            if x != " " and (x in "-+" or x in num) and len(res) == 0:
                res += x
            elif x in num:
                res += x
            else:
                break
        if res == "" or res in "-+":
            return 0
        else:
            return int(res)

    def multiply(self, num1: str, num2: str) -> str:
        a = self.myAtoi(num1)
        b = self.myAtoi(num2)
        return str(a * b)
