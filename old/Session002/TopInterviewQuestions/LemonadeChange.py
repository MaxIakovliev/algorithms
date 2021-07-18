class Solution:
    """
    https://leetcode.com/problems/lemonade-change/

    Explanation:
Count the number of $5 and $10 in hand.
If cutomer pay with $5: five++
If cutomer pay with $10: ten++, five--
If cutomer pay with $20: ten--, five-- or five -= 3
Check if five is positive, otherwise return false.
    """
    def lemonadeChange(self, bills: 'list[int]') -> bool:
        fives=0
        tens=0
        for amount in bills:
            if amount==5:
                fives+=1
            elif amount==10:
                fives-=1
                tens+=1
            elif tens>0:
                tens-=1
                fives-=1
            else:
                fives-=3
            if fives<0:
                return False
        return fives>=0
