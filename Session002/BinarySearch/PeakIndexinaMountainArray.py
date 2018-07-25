# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
class Solution(object):
    def peakIndexInMountainArray(self, a):
        """
        :type A: List[int]
        :rtype: int
        """
        lo=0
        hi=len(a)
        while lo<=hi:
            mid= (int)((lo+hi)/2)
            if mid-1>=0 and mid+1<len(a) and a[mid]>a[mid+1] and a[mid]>a[mid-1] :
                return mid
            elif mid>0 and  mid+1<len(a) and  a[mid]<a[mid-1]:
                hi=mid
            else:
                lo=mid+1
        return -1

if __name__ =="__main__":
    c=Solution()
    print(c.peakIndexInMountainArray( [0,1,2,-1]))
                
        
        