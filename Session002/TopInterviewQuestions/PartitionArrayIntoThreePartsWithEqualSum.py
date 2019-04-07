class Solution:
    def canThreePartsEqualSum(self, a):
        total_sum=0
        for item in a:
            total_sum+=item
        if total_sum%3!=0:
            return False

        s1=total_sum//3
        subsets=0
        count=0
        for item in a:
            count+=item
            if count==s1:
                subsets+=1
                count=0

        if subsets==3 and count==0:
            return True

        return False
        


if __name__ == "__main__":
    c=Solution()
    print(c.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))#true
    print(c.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))#false
    print(c.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))#true
    print(c.canThreePartsEqualSum([6,1,1,13,-1,0,-10,20]))#false
    print(c.canThreePartsEqualSum([18,12,-18,18,-19,-1,10,10]))#true

            
