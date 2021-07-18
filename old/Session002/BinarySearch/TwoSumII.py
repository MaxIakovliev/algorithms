class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            lo=i+1
            hi=len(numbers)
            while lo<hi:
                mid=(int)((lo+hi)/2)
                if numbers[i]+numbers[mid]==target:
                    return [i+1,mid+1]
                elif numbers[i]+numbers[mid]>target:
                    hi=mid
                else:
                    lo=mid+1
        return []
if __name__ =="__main__":
    c=Solution()
    print(c.twoSum([2,7,11,15],127))