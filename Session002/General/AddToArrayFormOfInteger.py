class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        a=0
        for i in range(len(A)):
            a=a*10+A[i]

        a+=K
        A=[]
        while a>0:
            t=a%10
            A.insert(0, t)
            a//=10
        if len(A)==0:
            return [0]
        return A

    def addToArrayForm2(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        if K==0:
            return A
        k=[]
        while K>0:
            t=K%10
            k.insert(0,t)
            K//=10
        
        extra=0
        aIdx=len(A)-1
        for i in range(len(k)-1,-1,-1):
            if aIdx<0:
                if extra>0:
                    t=k[i]+extra
                    extra=0
                    if t>=10:
                        A.insert(0,t%10)
                        extra=t//10
                    else:
                        A.insert(0,t)
                else:
                    A.insert(0,k[i])

            else:
                
                t=k[i]+A[aIdx]+extra
                extra=0
                if t>=10:
                    rem=t%10
                    A[aIdx]=rem
                    extra=t//10
                else:
                    A[aIdx]=t
                aIdx-=1
        
        while aIdx>=0:
            t=A[aIdx]+extra
            extra=0
            if t>=10:
                A[aIdx]=t%10
                extra=t//10
            else:
                A[aIdx]=t
            aIdx-=1
        
        if extra>0 and aIdx<0:
            A.insert(0,extra)
            return A

        if extra>0:
            t=A[0]+extra
            if t>=10:
                A[0]=t%10
                A.insert(0,t//10)
            else:
                A.insert(0,t)

        return A






if __name__=="__main__":
    c=Solution()
    print(c.addToArrayForm([1,2,0,0],34))
    print(c.addToArrayForm2([2,7,4],181))
    print(c.addToArrayForm2([9],181))
    print(c.addToArrayForm2([9],999))
    print(c.addToArrayForm2([9,9,9,9,9,9,9,9,9,9],1))
    print(c.addToArrayForm2([7,7,5,2],7105))
