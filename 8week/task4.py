"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/sliding-subarray-beauty/description
"""


class Solution:
    def getSubarrayBeauty(self, nums: list[int], k: int, x: int) -> list[int]:
        counter, ans = [0] * 50, [0] * (len(nums) - k + 1)
        for i in range(len(nums)):
            if nums[i] < 0:
                counter[nums[i] + 50] += 1
            if i - k >= 0 and nums[i - k] < 0:
                counter[nums[i - k] + 50] -= 1
            if i - k + 1 < 0:
                continue
            count = 0
            for j in range(50):
                count += counter[j]
                if count >= x:
                    ans[i - k + 1] = j - 50
                    break
        return ans
