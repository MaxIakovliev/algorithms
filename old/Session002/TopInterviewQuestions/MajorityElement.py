class Solution:
    def majorityElement(self, nums:list):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        val=0
        u={}
        for n in nums:
            if n not in u:
                u[n]=1
            else:
                u[n]+=1

            if count<u[n]:
                count=u[n]
                val=n
        return val
if __name__ =="__main__":
    c=Solution()
    print(c.majorityElement([2,2,1,1,1,2,2])) #2
    print(c.majorityElement([3,2,3])) #3