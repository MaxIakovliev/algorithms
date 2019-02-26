import math
class Solution(object):
    """
    https://leetcode.com/problems/k-closest-points-to-origin/
    formula: dist=sqrt((x2-x1)^2+(y2-y1)^2)
    """
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dist=[]
        for i in range(len(points)):
            dist.append(abs(math.sqrt((points[i][0]-0)**2+(points[i][1]-0)**2)))
        

        count=0
        res=[]
        usedIdx=set()
        while count<K:
            minSoFar=float('inf')
            selectedIdx=-1
            for m in range(len(dist)):
                if dist[m]<minSoFar and m not in usedIdx:
                    selectedIdx=m
                    minSoFar=dist[m]
            res.append(points[selectedIdx])
            usedIdx.add(selectedIdx)
            count+=1
        return res


    def kClosest2(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dist={}
        for i in range(len(points)):
            dist[abs(math.sqrt((points[i][0]-0)**2+(points[i][1]-0)**2))]=i
        res=[]
        count=0
        for kv in sorted(dist.items(), key=lambda x: x[0]):
            res.append(points[kv[1]])
            count+=1
            if count==K:
                break
        return res


if __name__=="__main__":
    c=Solution()
    print(c.kClosest2([[1,3],[-2,2]],1))#[-2,2]
    print(c.kClosest2([[3,3],[5,-1],[-2,4]],2))#[[3,3],[-2,4]]
