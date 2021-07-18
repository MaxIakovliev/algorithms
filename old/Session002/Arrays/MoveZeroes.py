class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return
        i=0
        j=len(nums)-1
        while nums[j]==0 and j>=0:
            j-=1
        while i<=j:
            
            if nums[i]==0:
                res=self.swap(nums,i,i+1)
                if res==False:
                    return
            i+=1
        return


    def swap(self, nums,i,j):
        if j==len(nums):
            return False
        while nums[j]==0:
            j+=1
            if j==len(nums):
                return False
        
        t=nums[i]
        nums[i]=nums[j]
        nums[j]=t
        return True

if __name__=="__main__":
    c=Solution()
    arr=[0,1,0,2,0,0,3,0,0,0]
    c.moveZeroes(arr)
    print(arr)
    arr=[0,0]
    c.moveZeroes(arr)
    print(arr)
    arr=[0,1]
    c.moveZeroes(arr)
    print(arr)

    
            