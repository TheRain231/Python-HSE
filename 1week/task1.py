#https://leetcode.com/problems/string-to-integer-atoi/?envType=problem-list-v2&envId=string

class Solution:
    def myAtoi(self, s: str) -> int:
        num = '0123456789'
        res = ''
        for x in s:
            if x == ' ' and len(res) == 0:
                continue
            if x != ' ' and (x in '-+' or x in num) and len(res) == 0:
                res += x
            elif x in num:
                res += x
            else:
                break
        if res == '' or res in '-+':
            return 0
        else:
            ans = int(res)
            if ans > 2147483647:
                ans = 2147483647
            elif ans < -2147483648:
                ans = -2147483648
            return ans