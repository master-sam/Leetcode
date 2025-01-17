"""
//Daily Question 29th July, 2024
Link: https://leetcode.com/problems/count-number-of-teams/description/
Description: There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

Constraints:
n == rating.length
3 <= n <= 1000
1 <= rating[i] <= 105
All the integers in rating are unique.

Python Code:
"""
class Solution:
    #TC: O(N^2)
    #SC: O(4*N)
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        nmap = [[0]*4 for _ in range(n)]
        for i in range(n-2, 0, -1):
            for j in range(n):
                if j < i:
                    if rating[j] > rating[i]:
                        nmap[i][1] += 1
                    else:
                        nmap[i][0] += 1
                elif j == i:
                    continue
                else:
                    if rating[j] > rating[i]:
                        nmap[i][3] += 1
                    else:
                        nmap[i][2] += 1


        # print(nmap)
        ans = 0
        for i in range(n-2, 0, -1):
            ans += nmap[i][0]*nmap[i][3] + nmap[i][1]*nmap[i][2]

        return ans
        #naive solution, giving TLE
        #TC: O(N^3)
        #SC: O(1)
        # n = len(rating)
        # ans = 0
        # for i in range(n-2):
        #     for j in range(i+1,n-1):
        #         for k in range(j+1,n):
        #             if rating[i]>rating[j]:
        #                 if rating[j] > rating[k]:
        #                     ans += 1
        #                 else:
        #                     continue
        #             else:
        #                 if rating[j] < rating[k]:
        #                     ans += 1
        #                 else:
        #                     continue

        # return ans

        
