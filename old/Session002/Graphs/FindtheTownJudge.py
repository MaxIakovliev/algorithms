class Solution:
    """
    https://leetcode.com/problems/find-the-town-judge/
    
    solution:
    https://leetcode.com/problems/find-the-town-judge/discuss/242938/JavaC%2B%2BPython-Directed-Graph

    """
    def findJudge(self, N: int, trust: "List[List[int]]") -> int:
        data=[0]*(N+1)
        for i,j in trust:
            data[i]-=1
            data[j]+=1

        for i in range(1, len(trust)):
            if data[i]==N-1:
                return i
        return -1
        