class Solution:
    """
    https://leetcode.com/problems/can-i-win/

n the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

Example

Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.





Solution:
https://leetcode.com/problems/can-i-win/discuss/155321/DFS-with-Memorization-Java-with-Explanations
Logical Thought
Whether 1st player can win with the current target sum(curDesiredTotal) and current choosable integers set(integersChoosable) can identify a state.
state(integersChoosable, curDesiredTotal) is true if 1st player can cause the running total to reach or exceed current target sum with current choosable integers set.
Aim state: state({1..maxChoosableInteger}, desiredTotal)
State transition:
1st player can pick any curInt from integersChoosable, and that will enable 2nd player to be with opponentState = integersChoosable_without_curInt and curDesiredTotal - curInt.
If 1st player can make any possible opponentState false, 1st player is promised to win, i.e., state(integersChoosable, curDesiredTotal) is true.

Please note that before we return true/false, we ought to set i unvisited.

Essence
Different from Solution for 486. Predict the Winner which track the state of the 1st player only and count the 2nd player's decision as influence, we track states of they both in this problem.

Code

    """
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        self.memo={}
        if desiredTotal<=maxChoosableInteger:
            return True
        if ((1 + maxChoosableInteger) / 2 * maxChoosableInteger) < desiredTotal:
            return False
        
        def can_i_win_in_this_situation(maxChoosableInteger, curDesiredTotal, chosen:[]):
            if curDesiredTotal<=0:
                return False
        
            chosenSerialization =tuple(chosen)
            if chosenSerialization in self.memo:
                return self.memo[chosenSerialization]
            
            for i in range(1, maxChoosableInteger+1):
                if chosen[i]:
                    continue
                chosen[i]=True
                if not can_i_win_in_this_situation(maxChoosableInteger,curDesiredTotal-i, chosen):
                    self.memo[chosenSerialization]=True
                    chosen[i]=False
                    return True
                chosen[i]=False
            self.memo[chosenSerialization]=False
            return False
        
        tmp=[False]*(maxChoosableInteger+1)
        return can_i_win_in_this_situation(maxChoosableInteger,desiredTotal,tmp)


        