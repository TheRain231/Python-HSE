"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/minimum-size-subarray-sum/description
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        currSum = 0
        minLength = float("inf")
        left = 0

        for right in range(n):
            currSum += nums[right]

            while currSum >= target:
                minLength = min(minLength, right - left + 1)
                currSum -= nums[left]
                left += 1

        if minLength == float("inf"):
            return 0
        return minLength
