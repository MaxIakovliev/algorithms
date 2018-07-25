class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        res=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    res.append(nums1[i])
                    del nums2[j]
                    break
        return res
                    
        
if __name__ =="__main__":
    c=Solution()
    print(c.intersect([1, 2, 2, 1],[2,2,3,1,1]))