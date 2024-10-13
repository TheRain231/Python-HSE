"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/3sum-closest/description/
"""


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        diff = float("inf")
        res = 0

        for i in range(n - 2):
            leftP, rightP = i + 1, n - 1
            while leftP < rightP:
                sum_val = nums[i] + nums[leftP] + nums[rightP]
                if sum_val > target:
                    rightP -= 1
                else:
                    leftP += 1
                value = abs(sum_val - target)

                if value < diff:
                    diff = value
                    res = sum_val

        return res
