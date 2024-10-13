"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/3sum/description/
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = set()
        n = len(nums)

        for i in range(n - 2):
            leftP = i + 1
            rightP = len(nums) - 1
            aim = -nums[i]

            while leftP < rightP:
                summ = nums[leftP] + nums[rightP]

                if summ == aim:
                    res.add((nums[i], nums[leftP], nums[rightP]))
                    leftP += 1
                    rightP -= 1

                    while leftP < rightP and nums[leftP] == nums[leftP - 1]:
                        leftP += 1
                    while leftP < rightP and nums[rightP] == nums[rightP + 1]:
                        rightP -= 1

                elif summ < aim:
                    leftP += 1
                else:
                    rightP -= 1

        return [list(item) for item in res]
