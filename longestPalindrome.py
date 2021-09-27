'''
Source:
https://leetcode.com/problems/longest-palindromic-substring/

Problem:
Given a string s, return the longest palindromic substring in s
'''

def longestPalindrome(s):
        n=len(s)
        
        #DP approach
        isPalindrome = [[0 for i in range(n)] for j in range(n)]

        maxLen = 0 
        maxStr = s[0]
        
        for i in range(n):
            isPalindrome[i][i] = 1
            if i<n-1:
                if s[i]==s[i+1]:
                    isPalindrome[i][i+1] = 2
                    maxLen=2
                    maxStr=s[i:i+2]

        for k in range(2, n):        
            for i in range(0, n-1):
                if (i+k)>=n:
                    break
                if s[i]==s[i+k] and isPalindrome[i+1][i+k-1]!=0:
                    isPalindrome[i][i+k] = isPalindrome[i+1][i+k-1]+2                   
                    if isPalindrome[i][i+k] > maxLen:
                        maxLen = isPalindrome[i][i+k]
                        maxStr = s[i:i+k+1]
        
                        
        return maxStr

print(longestPalindrome("cbbd"))


'''
Solution:
When P(i,j) is the length of the logest palindromic substring from s[i] to s[j],
P(i,j) = P(i-1,j+1) + 2
Since P(i,j) == P(j,i), I don't need to go through all possible pairs of i,j.
Also, since P(i-1, j+1) should be always present when calculating P(i,j), I need to calculate in diagonal order in the (n,n) matrix, starting from (1,1)...(n,n).  
'''
