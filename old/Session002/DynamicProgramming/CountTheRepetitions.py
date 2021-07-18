class Solution:
    """
    https://leetcode.com/problems/count-the-repetitions/

    solution: I dont understand it
    https://leetcode.com/problems/count-the-repetitions/discuss/95407/Simple-C%2B%2B-code-16-lines-but-slow-179ms
    """
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        m=len(s2)
        dp=[0]*m
        for i in range(m):
            start=i
            for char in s1:
                if char==s2[start%m]:
                    start+=1
            if start==i:
                return 0
            dp[i]=start-i
        idx=0
        for i in range(n1):
            idx+=dp[idx%m]
        return idx//m//n2

