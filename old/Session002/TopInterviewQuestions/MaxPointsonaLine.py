# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

import collections
class Solution:
    """
    https://leetcode.com/problems/max-points-on-a-line/description/
    """
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        def getGcd(a,b):
            if b==0:
                return a
            return getGcd (b, a%b)

        if len(points)<=2:
            return len(points)

        d=collections.defaultdict(int)
        result=0
        for i in range(len(points)):
            d.clear()
            overlap=0
            curmax=0
            for j in range(i+1, len(points)):
                dx=points[i].x-points[j].x
                dy=points[i].y-points[j].y
                if dx==0 and dy==0:
                    overlap+=1
                    continue
                gcd=getGcd(dx,dy)
                dx//=gcd
                dy//=gcd
                d[(dx,dy)]+=1
                curmax=max(curmax, d[(dx,dy)])
            result=max(result, curmax+overlap+1)
        return result