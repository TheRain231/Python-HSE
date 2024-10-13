"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/sort-colors/description
"""


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        c = {0: 0, 1: 0, 2: 0}
        for i in nums:
            c[i] = c.get(i, 0) + 1

        i = 0
        for v in c.keys():
            num = c[v]
            for j in range(i, i + num):
                nums[j] = v
            i += num
