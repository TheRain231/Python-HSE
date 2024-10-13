"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/container-with-most-water/description
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        leftP, rightP = 0, n - 1
        maxSquare = 0

        while leftP < rightP and leftP < n:
            square = min(height[leftP], height[rightP]) * (rightP - leftP)
            if square > maxSquare:
                maxSquare = square
            if height[leftP] < height[rightP]:
                leftP += 1
            else:
                rightP -= 1

        return maxSquare
