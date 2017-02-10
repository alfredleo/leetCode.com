# coding=utf-8
"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Total Accepted: 27937
Total Submissions: 39276
Difficulty: Easy
Contributors: Samuri
"""


class Solution(object):
    """
    >>> s = Solution()
    >>> s.hammingDistance(1,4)
    2
    """

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        pass


if __name__ == '__main__':
    import doctest

    doctest.testmod()
