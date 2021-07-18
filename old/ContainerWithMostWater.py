class ContainerWithMostWater:
    def maxArea(self, height):
        i,j=0,len(height)-1
        res=0
        while i<j:
            res=max(res,(j-i)*min(height[i],height[j]))
            if height[i]<height[j]:
                i+=1
            elif height[i]==height[j]:
                i+=1
                j-=1
            else:
                j-=1
        return res
                    