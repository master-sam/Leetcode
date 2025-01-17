"""
name: "Solution.py"

# DLC: 31 July 2024
# Link: https://leetcode.com/problems/filling-bookcase-shelves/description/?envType=daily-question&envId=2024-07-31

#Problem: 
You are given an array books where books[i] = [thicknessi, heighti] indicates the thickness and height of the ith book. You are also given an integer shelfWidth.

We want to place these books in order onto bookcase shelves that have a total width shelfWidth.

We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to shelfWidth, then build another level of the shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down. We repeat this process until there are no more books to place.

**Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.**

For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.
Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.

Constraints:

1 <= books.length <= 1000
1 <= thicknessi <= shelfWidth <= 1000
1 <= heighti <= 1000


#Solution:
"""
class Solution:
    #TC: O(N^2)
    #SC: O(N)
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0]*(n+1)
        for i,b in enumerate(books):
            dp[i+1] = dp[i] + b[1]
            w = b[0]
            h = b[1]
            for j in range(i-1, -1, -1):
                if books[j][0] + w <= shelfWidth:
                    h = max(books[j][1], h)
                    w += books[j][0]
                    dp[i+1] = min(dp[i+1], dp[j] + h)
                else:
                    break
            # print(dp)

        return dp[n]
        
