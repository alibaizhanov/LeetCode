class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss = ""
        repeat = len(s)
        j = 0
        rst = ""
        res = ""

        while j < repeat:
            for i in range(j,len(s)):
                ss = ss + s[i]
                if ss[::] == ss[::-1]:
                    rst = ss
            j = j + 1
            ss = ""
            if len(rst)>= len(res):
                    res = rst

        return res
