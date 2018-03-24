class LetterCombinationsOfPhoneNumber:
    def letterCombinations(self, digits):
        if len(digits)==0:
            return list()
        d={
            '0':'',
            '1':'',
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        res=['']
        for num in digits:
            candidate=d[num]
            if len(d[num])==0:
                continue
            tmp=[]
            for c in candidate:
                for cur in res:
                    tmp.append("{0}{1}".format(cur,c))
            res=tmp

        return res

    
 
c=LetterCombinationsOfPhoneNumber()
print(c.letterCombinations(""))    

        