"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/continuous-subarrays/description
"""
from functools import cache


class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        @cache
        def dp(i, maxnum, minnum):
            ans = 1
            if i >= 1:
                if nums[i] == nums[i - 1]:
                    ans += dp(i - 1, maxnum, minnum)
                if minnum <= nums[i - 1] < nums[i]:
                    ans += dp(i - 1, min(maxnum, nums[i - 1] + 2), minnum)
                if nums[i] < nums[i - 1] <= maxnum:
                    ans += dp(i - 1, maxnum, max(minnum, nums[i - 1] - 2))
            return ans

        return sum([dp(i, nums[i] + 2, nums[i] - 2) for i in range(len(nums))])
