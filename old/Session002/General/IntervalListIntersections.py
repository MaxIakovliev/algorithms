class Solution(object):
    """
    https://leetcode.com/problems/interval-list-intersections/

    Explanations:
    https://leetcode.com/articles/interval-list-intersections/#
    """
# Definition for an interval.
    class Interval(object):
        def __init__(self, s=0, e=0):
            self.start = s
            self.end = e

    def intervalIntersection(self, A, B):
        """
        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]
        """
        # Using merge approach from the  article of explanations
        i,j=0,0
        res=[]
        while i<len(A) and j<len(B):
            lo=max(A[i].start, B[j].start)
            hi=min(A[i].end,B[j].end)
            if lo<=hi:
                res.append(Interval(lo,hi))
            if A[i].end<B[j].end:
                i+=1
            else:
                j+=1
        return res


        