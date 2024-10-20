"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/bulls-and-cows/description
"""


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0

        d = [0] * 10

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                continue
            if d[int(secret[i])] < 0:
                cows += 1
            if d[int(guess[i])] > 0:
                cows += 1
            d[int(secret[i])] += 1
            d[int(guess[i])] -= 1
        return f"{bulls}A{cows}B"


a = Solution()
print(a.getHint("011", "110"))
