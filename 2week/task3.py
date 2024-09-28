"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/largest-number/description
"""


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums = [str(i) for i in nums]
        nums.sort(key=lambda x: x * 10, reverse=True)
        return "".join(nums).lstrip("0") or "0"
