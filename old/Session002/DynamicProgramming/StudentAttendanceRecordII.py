class Solution:

     """
     solution:
     https://leetcode.com/problems/student-attendance-record-ii/discuss/137060/Java-Fibonacci-Solution-O(n)-time-O(1)-space.
     """
     def checkRecord2(self, n: int) -> int:
          mod = 1000000007
          if n == 0:
               return 0
          a0 = [0]*(n+3)
          a1 = [0]*(n+3)
          a0[1], a0[2], a1[2] == 1, 1, 1
          for i in range(1, n+1):
               a0[i + 2] = (((a0[i - 1] + a0[i]) % mod) + a0[i + 1]) % mod
               a1[i + 2] = ((a0[i + 2] + a1[i - 1]) % mod + (a1[i] + a1[i + 1]) % mod) % mod

          return a1[-1]
