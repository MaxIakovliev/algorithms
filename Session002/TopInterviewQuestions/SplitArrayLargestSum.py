class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def valid(target,arr, b):
            count=1
            total=0 #?????
            for n in arr:
                total+=n
                if total>target:
                    total=n
                    count+=1
                    if count>b:
                        return False
            return True
                
                

        sumVal=0
        maxVal=0
        for n in nums:
            maxVal=max(maxVal,n)
            sumVal+=n
        if m==1:
            return sumVal
        hi=sumVal
        lo=maxVal
        while lo<hi:
            mid=(int)((lo+hi)/2)
            if valid(mid,nums,m):
                hi=mid
            else:
                lo=mid+1

        return lo

if __name__=="__main__":
    c=Solution()
    print(c.splitArray([7,2,5,10,8],2))
