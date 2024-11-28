"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description
"""


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        maxLen = 0
        zeroCount = 0
        left = 0

        for right in range(n):
            if nums[right] == 0:
                zeroCount += 1

            while zeroCount > 1:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1

            maxLen = max(maxLen, right - left)

        return maxLen
