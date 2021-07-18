class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        u=set()
        processed=set()
        nums2.sort()
        res=[]
        for n in nums1:
            if n in processed or n in u:
                continue
            lo=0
            hi=len(nums2)
            while lo<hi:
                mid=(int)((lo+hi)/2)
                if nums2[mid]==n:
                    u.add(n)
                    res.append(n)
                    break
                elif nums2[mid]>n:
                    hi=mid
                else:
                    lo=mid+1
            processed.add(n)
        return res

if __name__ =="__main__":
    c=Solution()
    print(c.intersection([1, 2, 2, 1],[5]))
                        

