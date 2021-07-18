# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def maxPoints(self, points):
        if points is None:
            return 0

        if len(points)<=2:
            return len(points)
        mp={}
        res=0
        for i in range(len(points)):
            mp.clear()
            overlap=0
            curMax=0
            j=i+1
            while j<len(points):
                x=points[j].x-points[i].x
                y=points[j].y-points[i].y
                if x==0 and y ==0:
                    overlap+=1
                    j+=1
                    continue
                g=self.gcd(x,y)
                if g!=0:
                    x=(int)(x/g)
                    y=(int)(y/g)
                if x in mp:
                    if y in mp[x]:
                        mp[x][y]=mp[x][y]+1
                    else:
                        mp[x][y]=1
                else:
                    tmp={}
                    tmp[y]=1
                    mp[x]=tmp
                curMax=max(curMax, mp[x][y])
                j+=1
            res=max(res, overlap+curMax+1)
        return res
    
    def gcd(self, a,b):
        if b==0:
            return a
        else:
            return self.gcd(b,a%b)


c=Solution()
print(c.maxPoints([Point(1,1),Point(3,2),Point(5,3),Point(4,1),Point(2,3),Point(1,4)]))


            
                        
