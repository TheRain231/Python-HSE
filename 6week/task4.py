"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/arithmetic-slices/description
"""


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n, subs = len(nums), 0
        lastDiff, count = None, 0

        for i in range(1, n):
            curDiff = nums[i] - nums[i - 1]
            if curDiff == lastDiff:
                subs += count
                count += 1
            else:
                lastDiff = curDiff
                count = 1

        return subs
