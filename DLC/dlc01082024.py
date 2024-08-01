"""
# 948. Bag of Tokens (https://leetcode.com/problems/bag-of-tokens/description/?envType=daily-question&envId=2024-07-31)
# description:

You start with an initial power of power, an initial score of 0, and a bag of tokens given as an integer array tokens, where each tokens[i] denotes the value of tokeni.

Your goal is to maximize the total score by strategically playing these tokens. In one move, you can play an unplayed token in one of the two ways (but not both for the same token):

Face-up: If your current power is at least tokens[i], you may play tokeni, losing tokens[i] power and gaining 1 score.
Face-down: If your current score is at least 1, you may play tokeni, gaining tokens[i] power and losing 1 score.
Return the maximum possible score you can achieve after playing any number of tokens.


#constraints:
Constraints:

0 <= tokens.length <= 1000
0 <= tokens[i], power < 104
Solution:
"""

class Solution:
  #TC: O(N)
  #SC: O(1)
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)
        i, j = 0, n-1
        maxi, ans = 0, 0
        while i <= j:
            if power < tokens[i] and ans > 0:
                power += tokens[j]
                j -= 1
                ans -= 1
                
            elif power >= tokens[i]:
                power -= tokens[i]
                i += 1
                ans += 1
                maxi = max(maxi, ans)
            else:
                break


        return maxi

        

