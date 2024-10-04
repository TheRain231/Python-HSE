"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description
"""


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        if n == 0:
            return [-1, -1]

        def slice(index):
            answer = []
            index1 = index
            while index1 > -1 and nums[index1] == target:
                index1 -= 1
            answer.append(index1 + 1)
            index1 = index
            while index1 < n and nums[index1] == target:
                index1 += 1
            answer.append(index1 - 1)
            return answer

        left = 0
        right = n

        while left <= right:
            mid = (right + left) // 2
            if mid >= n:
                return [-1, -1]
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return slice(mid)
        return [-1, -1]
