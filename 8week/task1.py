"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/description
"""
import math


class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        left = right = 0
        n = len(arr)
        curSum = 0
        m = [math.inf] * n
        res = math.inf

        for right in range(n):
            curSum += arr[right]
            while curSum > target:
                curSum -= arr[left]
                left += 1
            if curSum == target:
                if left > 0 and m[left - 1] != math.inf:
                    res = min(res, m[left - 1] + (right - left + 1))
                m[right] = min(m[right - 1], right - left + 1)
            else:
                m[right] = m[right - 1]

        return res if res != math.inf else -1
