"""
#DL: 30 July

# Problem:
You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

Constraints:

1 <= s.length <= 105
s[i] is 'a' or 'b'​​.


#Soulution:
"""

class Solution:
    #TC: O(N)
    #SC: (1)
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        b_c = 0
        ans = 0
        for i in range(n):
            if s[i] == 'a' and b_c > 0:
                b_c -= 1
                ans += 1
            elif s[i] == "b":
                b_c += 1
        return ans

        
