class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        def swap(arr, x,y):
            arr[x],arr[y]=arr[y],arr[x]
        o=1 #нечетное число
        e=0 #четное число
        while(o<len(A) and e<len(A)):
            if A[e]%2!=0:
                swap(A,o,e)
                o+=2
            else:
                e+=2
        return A

