class Solution:
    """
    https://leetcode.com/problems/remove-k-digits/
    """
    def removeKdigits(self, num: str, k: int) -> str:
        """
        basic idea: if current element < element at stack top，pop stack
         else keep pushing

        """
        if k>=len(num):
            return "0"
        st=[]#stack 
        cur=0
        for i in range(len(num)):
            while cur<k and len(st)>0 and int(num[i])<int(num[st[-1]]):
                st.pop()
                cur+=1
            st.append(i)
        res=""
        for idx in st:
            res+=num[idx]
        res+=num[st[-1]+1::]
        res=res.lstrip('0')
        if res and  cur<k:
            return res[:len(num)-k]
        return res if res else "0"
if __name__ == "__main__":
    c=Solution()
    print(c.removeKdigits("1432219",3))
        