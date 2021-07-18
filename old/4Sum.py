class FourSum:
    def fourSum(self, nums, target):
        if len(nums)<4:
            return list()
        
        nums.sort()
        res=list()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            while j<len(nums)-2:
                if j>i+1 and nums[j]==nums[j-1]:
                    j+=1
                    continue
                lo=j+1
                hi=len(nums)-1
                while lo<hi:
                    tmp=nums[i]+nums[j]+nums[lo]+nums[hi]
                    if tmp==target:
                        addNew=True
                        if len(res)>0:
                            prev=res[len(res)-1]
                            if prev[0]==nums[i] and prev[1]==nums[j] and prev[2]==nums[lo] and prev[3]==nums[hi]:
                                addNew=False
                        if addNew==True:
                            tlst=[nums[i],nums[j],nums[lo],nums[hi]]
                            res.append(tlst)
                        lo+=1
                        hi-=1
                    elif tmp<target:
                        lo+=1
                    else:
                        hi-=1
                    
                j+=1
        return res
        

if __name__=='__main__':
    f=FourSum()
    
    res=f.fourSum([-3,-2,-1,0,0,1,2,3],0)
    print(res)
    print('expected 8-  actual '+str(len(res)))






























        # if len(nums) == 0:
        #     return list()
        # nums.sort()
        # res = list()
        # for i in range(len(nums)):
        #     tmp = nums[i]+nums[i+1]+nums[i+2]+nums[i+3]
        #     if tmp > target:  # value too big- stop search
        #         return res

        #     tmp = nums[i]+nums[len(nums)-1] + \
        #         nums[len(nums)-2]+nums[len(nums)-3]
        #     if tmp < target:  # value too small
        #         continue
            
        #     j=i+1
        #     while i< len(nums)-2:
        #         tmp=nums[i]+nums[j]+nums[j+1]+nums[j+2]
        #         if tmp>target: # result too big
        #             return res
                
        #         if nums[i]+nums[j]+nums[len(nums)-2]+nums[len(nums)-1]<target:
        #             continue
                
        #         lo=j+1
        #         hi=len(nums)-1
        #         while lo<hi:
        #             tmp=nums[i]+nums[j]+nums[lo]+nums[hi]
        #             if tmp==target:
        #                 tlist=[nums[i],nums[j],nums[lo],nums[hi]]
        #                 res.append(tlist)
        #                 lo+=1
        #                 hi-=1
        #             elif tmp<target:
        #                 lo+=1
        #             else:
        #                 hi-=1
        # return res

