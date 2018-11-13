class Solution:
    """
    https://leetcode.com/problems/valid-number/discuss/23728/A-simple-solution-in-Python-based-on-DFA?page=1
    """
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        states=[{},
              {'blank': 1, 'sign': 2, 'digit':3, '.':4}, 
              {'digit':3, '.':4},
              {'digit':3, '.':5, 'e':6, 'blank':9},
              {'digit':5},
              {'digit':5, 'e':6, 'blank':9},
              {'sign':7, 'digit':8},
              {'digit':8},
              {'digit':8, 'blank':9},
              {'blank':9}
            ]
        currentState=1
        for c in s:
            if c>='0'and c<='9':
                c="digit"
            if c in ["-","+"]:
                c="sign"
            if c==" ":
                c="blank"
            if c not in states[currentState].keys():
                return False
            currentState = states[currentState][c]
        if currentState not in [3,5,8,9]:
            return False
        return True