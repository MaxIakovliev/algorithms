class Solution:
    """
    https://leetcode.com/problems/predict-the-winner/

Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Example 1:

Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return False.

Example 2:

Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.

Note:

    1 <= length of the array <= 20.
    Any scores in the given array are non-negative integers and will not exceed 10,000,000.
    If the scores of both players are equal, then player 1 is still the winner.


solution:
Suppose dp[l] represents best score for nums[l:]. And l and r are left and right index of current checking range. Score is P1's score - P2's score. So eventually if score >= 0, P1 wins.
So when it's P1's turn, dp actually represents P2's best score. So if P1 picks nums[l], P1's score is nums[l]-P2's best score of nums[l+1:] or nums[l] - dp[l+1]. Otherwise P2 picks nums[r], P1's score is nums[l]-P2's best score of nums[l:] or nums[r] - dp[l].
And as we are using bottom up for dp update, we initialized l = r-1 and keep expanding l to the left.
https://leetcode.com/problems/predict-the-winner/discuss/236645/DP-Complexity%3AO(n2)-Space%3AO(n)-solution

    """
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp=[0]*(len(nums)+1)
        for i in range(1, len(nums)):
            for j in range(len(nums)-i):
                dp[j]=max(nums[j]-dp[j+1], nums[j+i]-dp[j])
        return dp[0]>=0
        