"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximize-the-confusion-of-an-exam/description
"""


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        maxConsecutive = 0
        maxСount = 0

        counts = {"T": 0, "F": 0}
        left = right = 0

        while right < n:
            counts[answerKey[right]] += 1
            maxСount = max(maxСount, counts[answerKey[right]])

            if (right - left + 1) - maxСount > k:
                counts[answerKey[left]] -= 1
                left += 1

            maxConsecutive = max(maxConsecutive, right - left + 1)
            right += 1

        return maxConsecutive
