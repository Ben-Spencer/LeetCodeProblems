#Reverse Integer
"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        else:
            x = list(str(x))
            x = x[::-1]
            while x[0] == "0":
                x.pop(0);
            if x[-1] == "-":
                x.pop()
                x.insert(0,"-")
            x = "".join(x)
            x = int(x)
            if x > 2147483648 or x < -2147483648:
                return 0
            return x
