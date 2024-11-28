"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/k-radius-subarray-averages/description
"""


class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        ans = [0]
        for i in range(len(nums)):
            ans.append(ans[i] + nums[i])
        return [
            -1
            if i < k or i > len(nums) - 1 - k
            else (ans[i + k + 1] - ans[i - k]) // (2 * k + 1)
            for i in range(len(nums))
        ]
