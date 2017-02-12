# coding=utf-8
from utils import performance

"""
Find the largest palindrome made from the product of two n-digit numbers.
Since the result could be very large, you should return the largest palindrome mod 1337.

Example:
Input: 2
Output: 987

Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Note:
The range of n is [1,8].

Total Accepted: 890
Total Submissions: 5238
Difficulty: Easy
Contributors: arash2012
"""


class Solution(object):
    """
    >>> s = Solution()
    >>> s.largestPalindrome(2)
    987
    """
    def largestPalindrome(self, n):
        """
        :param n: int
        :return: int
        """
        return 0


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
