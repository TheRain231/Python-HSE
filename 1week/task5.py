"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/basic-calculator-ii/description
"""


class Solution:
    def calculate(self, s):
        def update():
            if sign == "+":
                stack.append(int(num))
            elif sign == "-":
                stack.append(-int(num))
            elif sign == "*":
                stack.append(stack.pop() * int(num))
            elif sign == "/":
                stack.append(int(stack.pop() / int(num)))

        num = ""
        stack = []
        sign = "+"

        for i in s:
            if i.isdigit():
                num += i
            elif i in "+-*/":
                update()
                num = ""
                sign = i
        update()
        return sum(stack)
