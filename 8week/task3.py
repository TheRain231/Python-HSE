"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-nice-subarray/description
"""


class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        left, right = 0, 1

        usedBits = nums[0]
        longestNice = 1
        while right < n:
            while right < n and usedBits & nums[right] == 0:
                usedBits |= nums[right]
                right += 1
            longestNice = max(longestNice, right - left)
            usedBits ^= nums[left]
            left += 1

        return longestNice
