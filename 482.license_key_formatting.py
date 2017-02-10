# encoding: utf-8
from cStringIO import StringIO

"""
Now you are given a string S, which represents a software license key which we would like to format. The string S is
 composed of alphanumerical characters and dashes. The dashes split the alphanumerical characters within the string
 into groups. (i.e. if there are M dashes, the string is split into M+1 groups). The dashes in the given string are
 possibly misplaced.
We want each group of characters to be of length K (except for possibly the first group, which could be shorter, but
 still must contain at least one character). To satisfy this requirement, we will reinsert dashes. Additionally, all
 the lower case letters in the string must be converted to upper case.
So, you are given a non-empty string S, representing a license key to format, and an integer K. And you need to return
 the license key formatted according to the description above.

Example 1:
Input: S = "2-4A0r7-4k", K = 4
Output: "24A0-R74K"
Explanation: The string S has been split into two parts, each part has 4 characters.

Example 2:
Input: S = "2-4A0r7-4k", K = 3
Output: "24-A0R-74K"
Explanation: The string S has been split into three parts, each part has 3 characters except the first part as it could be shorter as said above.

Note:
The length of string S will not exceed 12,000, and K is a positive integer.
String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
String S is non-empty.

Total Accepted: 7087
Total Submissions: 17021
Difficulty: Medium
Contributors: aizj_Forever

"""

__author__ = 'alfredleo@gmail.com (Alfred)'


class Solution(object):
    """
    >>> sol = Solution()
    >>> print sol.licenseKeyFormatting7("2-4A0r7-4k",4)
    24A0-R74K
    >>> print sol.licenseKeyFormatting7("2-4A0r7-4k",3)
    24-A0R-74K
    """

    def licenseKeyFormatting(self, S, K):
        """
        Beats 17.29% submissions on 10.02.2017 (216 ms)
        :type S: str
        :type K: int
        :rtype: str
        """
        formatted = ''
        step = 0
        S = S.replace('-', '').upper()
        for c in reversed(S):
            if step % K == 0 and step != 0:
                formatted = '-' + formatted
            formatted = c + formatted
            step += 1
        return formatted

    def licenseKeyFormatting1(self, S, K):
        """
        Beats 3.12% submissions on 10.02.2017 (392 ms)
        :type S: str
        :type K: int
        :rtype: str
        """
        formatted = []
        step = 0
        S = S.replace('-', '').upper()
        for c in reversed(S):
            if c != '-':
                if step % K == 0 and step != 0:
                    formatted.insert(0, '-')
                formatted.insert(0, c.upper())
                step += 1
        return ''.join(formatted)

    def licenseKeyFormatting2(self, S, K):
        """
        Beats 29.91% submissions on 10.02.2017 (172 ms)
        :type S: str
        :type K: int
        :rtype: str
        """
        formatted = ''
        step = 0
        S = S.replace('-', '').upper()
        for c in reversed(S):
            if step % K == 0:
                formatted = '-' + formatted
            formatted = c + formatted
            step += 1
        return formatted[:-1]

    def licenseKeyFormatting3(self, S, K):
        """
        Beats 76.17% submissions on 10.02.2017 (49 ms)
        :type S: str
        :type K: int
        :rtype: str
        """
        formatted = []
        S = S.replace('-', '').upper()
        for i in xrange(len(S), 0, -K):
            start = i - K
            if start < 0:
                start = 0
            formatted.insert(0, '-' + S[start:i])
        return ''.join(formatted)[1:]

    def licenseKeyFormatting4(self, S, K):
        """
        Beats 90.58% submissions on 10.02.2017 (42 ms)
        :type S: str
        :type K: int
        :rtype: str
        """
        formatted = []
        S = S.replace('-', '')
        for i in xrange(len(S), 0, -K):
            start = i - K
            if start < 0:
                start = 0
            formatted.insert(0, '-' + S[start:i].upper())
        return ''.join(formatted)[1:]

    def licenseKeyFormatting5(self, S, K):
        """
        Beats 97.59% - 66.51% submissions on 10.02.2017 (39-58 ms)
        It seems like the % varies depending on the server load of leetcode.
        :type S: str
        :type K: int
        :rtype: str
        """
        file_str = StringIO()
        S = S.replace('-', '')
        start = len(S) % K
        for i in xrange(start, len(S), K):
            file_str.write(S[i:i + K].upper() + '-')
        remaining = ''
        if start != 0:
            remaining = S[0:start].upper() + '-'
        return (remaining + file_str.getvalue())[:-1]

    def licenseKeyFormatting6(self, S, K):
        """
        The most pythonic and fast implementation
        author: realisking
        :type S: str
        :type K: int
        :rtype: str
        """
        S = "".join(S.upper().split("-"))
        end = len(S) % K
        ans = "-".join([S[:end]] + [S[i:i + K] for i in range(end, len(S), K)])
        return ans.lstrip("-")

    def licenseKeyFormatting7(self, S, K):
        """
        Beats 89% submissions on 10.02.2017 (50 ms)
        author: zqfan
        :type S: str
        :type K: int
        :rtype: str
        """
        s = S.replace('-', '').upper()[::-1]
        return '-'.join([s[i:i + K] for i in xrange(0, len(s), K)])[::-1]


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
