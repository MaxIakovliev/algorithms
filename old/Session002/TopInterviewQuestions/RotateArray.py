class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k==0:
            return
        if k>len(nums):
            k=k%len(nums)
        tmp=[nums[i] for i in range(len(nums)-k,len(nums))]
        end=len(nums)-1
        start=len(nums)-k-1
        while start>=0:
            nums[end]=nums[start]
            start-=1
            end-=1
        
        for i in range(len(tmp)):
            nums[i]=tmp[i]


       
if __name__=="__main__":
    c=Solution()
    arr=[1,2,3,4,5,6,7]
    c.rotate(arr,3)
    print(arr)

    arr=[-1,-100,3,99]
    c.rotate(arr,2)
    print(arr)

    arr=[1,2]
    c.rotate(arr,1)
    print(arr)