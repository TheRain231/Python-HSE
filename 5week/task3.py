"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/integer-to-roman/desription
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = [
            "M",
            "CM",
            "D",
            "CD",
            "C",
            "XC",
            "L",
            "XL",
            "X",
            "IX",
            "V",
            "IV",
            "I",
        ]

        s = ""
        i = 0

        while num > 0:
            if num >= numbers[i]:
                s += symbols[i]
                num -= numbers[i]
            else:
                i += 1
        return s
