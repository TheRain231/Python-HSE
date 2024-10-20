"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/desription
"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        dictionary = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }
        digits = list(map(int, digits))
        s = []
        for digit in digits:
            s.append(dictionary[digit])

        ans = []
        n = len(digits)
        indices = [0] * n

        if len(indices) == 0:
            return ans

        while True:
            cur = ""
            for i in range(len(indices)):
                cur += s[i][indices[i]]
            ans.append(cur)

            indices[-1] += 1
            for i in range(len(indices) - 1, -1, -1):
                if indices[i] >= len(s[i]):
                    if i == 0:
                        return ans
                    indices[i] = 0
                    indices[i - 1] += 1
