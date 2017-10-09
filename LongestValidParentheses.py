# coding=utf-8
# __author__ = 'xhm'

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []

        for i in range(len(s)):

            if s[i] == '(':
                stack.append(i)
            if s[i] == ')':
                if stack:
                    if s[stack[-1]] == '(':
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
        ans = 0
        if stack:
            ans = stack[0] - ans
            for i in range(1, len(stack)):
                temp = stack[i] - stack[i - 1] - 1
                if temp > ans:
                    ans = temp
            temp = len(s) - stack[-1] - 1
            if temp > ans:
                ans = temp
        else:
            ans = len(s)

        return ans