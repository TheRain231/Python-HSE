"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/jump-game-ii/description
"""


class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        i = 0
        count = 0
        if n == 1:
            return 0
        while i < n:
            num = nums[i]
            if num + i + 1 >= n:
                count += 1
                break
            nextNum = 0
            nextI = 0
            for j in range(i + 1, i + num + 1):
                if nums[j] + j >= nextNum:
                    nextNum = nums[j] + j
                    nextI = j
            i = nextI
            count += 1
        return count
