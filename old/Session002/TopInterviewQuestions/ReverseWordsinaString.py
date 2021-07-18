class Solution(object):
    """
    https://leetcode.com/problems/reverse-words-in-a-string/description/
    """
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def swap(arr, x,y):
            arr[x],arr[y]=arr[y],arr[x]

        if s is None or len(s)==0:
            return s

        s=s.strip()
        while '  ' in s:
            s=s.replace('  ',' ')
        splt=s.split(' ')
        i=0
        j=len(splt)-1
        while i<j:
            swap(splt,i,j)
            i+=1
            j-=1

        return ' '.join(splt)

if __name__=="__main__":
    c=Solution()
    print(c.reverseWords("the sky is blue"))#blue is sky the
            

        