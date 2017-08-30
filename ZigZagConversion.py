# coding=utf-8
# __author__ = 'xhm'


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        start = numRows * 2 - 2
        if start == 0:
            return s
        ans = ""
        for rows in range(numRows):
            number = rows
            move = start - rows * 2
            while number < len(s):
                ans += s[number]
                number += move
                if move == 0:
                    move = start - move
                    number += move
                else:
                    move = start - move
        return ans

