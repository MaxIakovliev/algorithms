import sys
class ThreeSumClosest:
    def threeSumClosest(self, nums, target):
        i=0
        j=0
        k=0
        res=sys.maxsize
        min_sum=sys.maxsize
        while i<len(nums):
            j=i+1
            while j<len(nums):
                k=j+1
                while k< len(nums):
                    tmp=nums[i]+nums[j]+nums[k]
                    if (abs(target-tmp)<min_sum):
                        res=tmp
                        min_sum=abs(target-tmp)
                    k+=1
                j+=1
            i+=1
        return res

    def threeSumClosest2(self, nums, target):
        nums.sort()
        i=0
        res=nums[0]+nums[1]+nums[2]
        while i<len(nums):
            j=i+1
            k=len(nums)-1
            while k>j:
                tmp=nums[i]+nums[j]+nums[k]
                if abs(target-tmp)<abs(target-res):
                    res=tmp
                if tmp<target:
                    j+=1
                elif tmp>target:
                    k-=1
                else:
                    return res
            i+=1

        return res

if __name__ =='__main__':
    c=ThreeSumClosest()
    # print(c.threeSumClosest2([1,1,1,0],100))
    print(c.threeSumClosest2([0,1,2],0))