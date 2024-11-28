"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximum-erasure-value/description
"""


class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        ans, curSum = 0, 0
        eleMap = {}
        arr = []
        for e in nums:
            if eleMap.get(e, False):
                while arr and arr[0] != e:
                    v = arr.pop(0)
                    curSum -= v
                    del eleMap[v]
                arr.pop(0)
                arr.append(e)
            else:
                arr.append(e)
                eleMap[e] = 1
                curSum += e
            ans = max(ans, curSum)
        return ans
