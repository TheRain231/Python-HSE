"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/repeated-dna-sequences/description
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        ans = set()
        seen = set()

        for i in range(len(s) - 9):
            dna = s[i : i + 10]
            if dna in seen:
                ans.add(dna)
            seen.add(dna)

        return list(ans)
