class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        i=0
        res=[]
        curLen=1
        while i<len(nums):
            shift=0
            while  shift<len(nums):
                curLen=1
                if i+shift>=len(nums):
                    break                    
                while curLen<=len(nums):
                    tmp=[]
                    for j in range(i+shift, i+shift+curLen):
                        if j>=len(nums):
                            break
                        tmp.append(nums[j])
                    
                    res.append(tmp)

                    curLen+=1
                shift+=1
            
            i+=1


        res.append([])
        return list(res)
    
if __name__=="__main__":
    c=Solution()
    print(c.subsets([1,2,3]))

            
