"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/subarrays-with-k-different-integers/description
"""


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def f(x):
            pos = [0] * len(nums)
            count = {}
            j = 0
            for i in range(len(nums)):
                count[nums[i]] = count.get(nums[i], 0) + 1
                while len(count) > x:
                    count[nums[j]] = count.get(nums[j], 0) - 1
                    if count[nums[j]] == 0:
                        count.pop(nums[j])
                    j += 1
                pos[i] = j
            return pos

        pos1, pos2 = f(k - 1), f(k)
        answer = 0
        for i in range(len(pos1)):
            answer += pos1[i] - pos2[i]
        return answer
