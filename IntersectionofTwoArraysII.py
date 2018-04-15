class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        i=0
        res=list()
        if len(nums1)==0 or len(nums2)==0:
            return res

        while i<len(nums1):
            idx=self.binSearch(nums1[i],nums2)
            if idx is None:
                return res
            if idx<0:
                i+=1
            else:
                res.append(nums2[idx])
                del nums2[idx]
                i+=1
        return res
            
    
    def binSearch(self, val, nums1):
        min=0
        max=len(nums1)-1
        if len(nums1)==0 or val> nums1[len(nums1)-1] or val<nums1[0]:
            return -1
        if len(nums1)==1 and nums1[0]==val:
            return 0
        # else:
        #     return -1

        
        while(min<max):
            avg=0
            ln=len(nums1[min:max])
            if len(nums1[min:max])%2==0:
                avg= min+(int)((max-min )/2)
            else:
                avg= min+(int)((max-min )/2)+1
            
            if ln==1 and nums1[min]==val:
                return min
                

            if ln==2:
                if nums1[min]==val:
                    return min
            if nums1[max]==val:
                return max
                             
            if nums1[avg]==val:
                return avg
            if nums1[avg]>val:
                if avg==max:
                    return -1
                max=avg
            else:
                if avg==min:
                    return -1
                min=avg
        return -1
            
            
       

if __name__ =="__main__":
    c=Solution()
    # a=[1,2,3,3,4,5]
    # b=[1,2,3,4,3,5]
    # res=c.intersect(a,b)
    # print(res)
                
    # a=[-2147483648,1,2,3]
    # b=[1,-2147483648,-2147483648]
    # res=c.intersect(a,b)
    # print(res)

    # a=[1]
    # b=[1,2]
    # res=c.intersect(a,b)
    # print(res)


    # a=[1]
    # b=[1]
    # res=c.intersect(a,b)
    # print(res)

    # a=[1]
    # b=[1,1]
    # res=c.intersect(a,b)
    # print(res)

    a=[4,9,5]
    b=[9,4,9,8,4]
    res=c.intersect(a,b)
    print(res)

    # a=[]
    # b=[1,2]
    # res=c.intersect(a,b)
    # print(res)


    # a=3
    # b=[0,1,2,3,4]
    # res=c.binSearch(a,b)
    # print(res)

    # for i in range(6):
    #     lst=list(range(i))
    #     for j in range (7):
    #         print(j)
    #         print(lst)
    #         k=c.binSearch(j,lst)
    #         print(k)
    #         print('-------------------')
        # print(lst)
