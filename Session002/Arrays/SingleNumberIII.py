class Solution:
    """
    https://leetcode.com/problems/single-number-iii/description/
    """
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        t={}
        for n in nums:
            if n in t:
                t[n]+=1
            else:
                t[n]=1

            if t[n]==2:
                del t[n]
        res=[]
        for key,val in t.items():
            res.append(key)
        return res

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d=set()
        for n in nums:
            if n in d:
                d.remove(n)
            else:
                d.add(n)
        return list(d)
if __name__=="__main__":
    c=Solution()
    print(c.singleNumber([1,2,1,3,2,5])) #[3,5]
