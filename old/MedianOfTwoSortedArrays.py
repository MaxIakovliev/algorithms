class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res=list()
        i=0
        j=0
        while i<len(nums1) or j<len(nums2):
            if i<len(nums1) and j<len(nums2):
                if nums1[i]<nums2[j]:
                    res.append(nums1[i])
                    i+=1
                else:
                    res.append(nums2[j])
                    j+=1
            elif i<len(nums1) and j>=len(nums2):
                res.append(nums1[i])
                i+=1
            elif i>=len(nums1) and j< len(nums2):
                res.append(nums2[j])
                j+=1
        
        if len(res)%2==0:
            return (res[(int)(len(res)/2)]+res[(int)(len(res)/2)-1])/2
        else:
            return res[(int)(len(res)/2)]

if __name__ =='__main__':
    c=Solution()
    nums1 = [1, 3]
    nums2 = [2]
    res=c.findMedianSortedArrays(nums1,nums2)
    print(res)

    nums1 = [1, 2]
    nums2 = [3, 4]
    res=c.findMedianSortedArrays(nums1,nums2)
    print(res)

    
