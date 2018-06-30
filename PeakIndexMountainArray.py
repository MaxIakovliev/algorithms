class Solution:
    def peakIndexInMountainArray(self, a):
        """
        :type A: List[int]
        :rtype: int
        """
        lo=0
        hi=len(a)
        while (lo<hi):
            mid=(int)((hi+lo)/2)
            if mid-1>=0 and mid+1<len(a) and a[mid-1]<a[mid] and a[mid]>a[mid+1]:
                return mid
            elif mid-1>=0 and mid+1<len(a) and a[mid-1]<a[mid] and a[mid]<a[mid+1]:
                lo=mid+1
            else:
                hi=mid
        
        return -1


if __name__=="__main__":
    c=Solution()
    print(c.peakIndexInMountainArray([-1,0,1,-1]))        
    print(c.peakIndexInMountainArray([0,2,1,0]))        

    
                