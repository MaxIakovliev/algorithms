class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        self.morze=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        self.idx={}
        self.buildIdx()
        res=set()
        for word in words:
            res.add(self.toMorze(word))
        return len(res)
        
    def buildIdx(self):
        start='a'
        count=0
        while count<26:
            self.idx[start]=self.morze[count]
            count+=1
            start=chr(ord(start)+1)


    def toMorze(self, word):
        res=[]
        for c in str(word).lower():
            res.append(self.idx[c])
        return "".join(res)

if __name__=='__main__':
    c=Solution()
    print(c.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
                
