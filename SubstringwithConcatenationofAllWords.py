# coding=utf-8
# __author__ = 'xhm'


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        repeat_list = []
        length = len(words[0])
        start = 0
        ans = []
        while start < len(s)-length+1:
            for i in range(len(words)):
                s_start = start + i * length
                s_end = start + i * length + length
                if s[s_start:s_end] in words:
                    if s[s_start:s_end] in repeat_list:
                        if words.count(s[s_start:s_end]) <= repeat_list.count(s[s_start:s_end]):
                            repeat_list = []
                            start += 1
                            break
                    repeat_list.append(s[s_start:s_end])
                    if len(repeat_list) == len(words):
                        ans.append(start)
                        start += 1
                        repeat_list = []
                        break
                else:
                    repeat_list = []
                    start += 1
                    break

        return ans
