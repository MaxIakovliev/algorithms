class Solution:
    """
    https://leetcode.com/problems/3sum/
    """
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        res=[]
        nums.sort()
        u=set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        tmp=[nums[i],nums[j],nums[k]]
                        tmp.sort()
                        key=str(tmp)
                        if key not in u:
                            res.append(tmp)
                            u.add(key)
        return res

    def threeSum2(self, nums: 'List[int]') -> 'List[List[int]]':
        res=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                s=nums[i]+nums[left]+nums[right]
                if s<0:
                    left+=1
                elif s>0:
                    right-=1
                else:
                    res.append((nums[i],nums[left],nums[right]))
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
        return res

        
       
if __name__ == "__main__":
    c=Solution()
    print(c.threeSum2([-1, 0, 1, 2, -1, -4]))
    print(c.threeSum2([-5,-1,10,-15,10,-11,-8,-14,5,3,9,3,-11,-4,0,5,5,1,14,2,-13,0,-10,-12,-2,4,-9,-7,14,-2,3,-6,13,-10,-14,8,-14,-15,1,7,4,-5,-13,8,-1,-6,-10,-11,10,11,6,13,-4,11,-14,1,1,14,9,-8,-2,-11,1,-12,-14,-6,3,10,-6,-11,-6,5,-9,-4,-10,5,5,-5,1,1,13,-8,-1,-14,-11,-8,2,-3,-9,-12,4,4,14,12,-1,8,-9,-13,3,0,13,12,-9,12,-7,-12,2,5,-1,-11]
))
        