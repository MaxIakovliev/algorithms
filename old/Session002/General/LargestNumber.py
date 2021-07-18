class Solution(object):
    """
    https://leetcode.com/problems/largest-number/
    
    good explanation here:
    https://leetcode.com/problems/largest-number/discuss/53298/Python-different-solutions-(bubble-insertion-selection-merge-quick-sorts)
    """
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(n1, n2):
            return str(n1)+str(n2)>str(n2)+str(n1)

        def bubble_sort(nums):
            for  i in range(len(nums),0,-1):
                for j in range(i-1):
                    if not compare(nums[j], nums[j+1]):
                        nums[j],nums[j+1]=nums[j+1],nums[j]
            return str(int("".join(map(str,nums))))

        def merge_sort(nums, l,r):
            if l>r:
                return
            if l==r:
                return [nums[l]]
            mid=(l+r)//2
            left=merge_sort(nums,l,mid)
            right=merge_sort(nums,mid+1,r)
            return merge(left, right)
        
        def merge(left, right):
            res,i,j=[],0,0
            while i<len(left)and j<len(right):
                if not compare(left[i],right[j]):
                    res.append(right[j])
                    j+=1
                else:
                    res.append(left[i])
                    i+=1
            res.extend(left[i:] or right[j:])
            return res

        # return bubble_sort(nums)
        nums= merge_sort(nums,0,len(nums)-1)
        return str(int("".join(map(str, nums))))


if __name__=="__main__":
    c=Solution()
    print(c.largestNumber([10,2]))
    print(c.largestNumber([3,30,34,5,9]))
        