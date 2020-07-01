#Count and Say
"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'

        prev=self.countAndSay(n-1)
        ans=''
        freq=1
        temp=prev[0]

        if len(prev)==1:
            return '11'
        for i in range(1,len(prev)):
            if prev[i]==temp:
                freq+=1
                if i+1>len(prev)-1:
                    ans+=str(freq)+temp

            else:
                ans+=str(freq)+temp
                temp=prev[i]
                freq=1
                if i+1>len(prev)-1:
                    ans+=str(freq)+temp
        return ans
