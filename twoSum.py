'''
Source:
https://leetcode.com/problems/two-sum/

Problem:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
'''

class Solution:
    def twoSum_naive(self, nums: List[int], target: int) -> List[int]:
        n=0
        for i in range(len(nums)-1):
            n+=1
            num2 = target - nums[i]
            if num2 in nums[i+1:]:
                return [i, nums[i+1:].index(num2)+n]
        
        return []

    def twoSum_hash(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            num2 = target - nums[i]
            if num2 in dic:
                return [dic[num2], i]
            if num[i] not in dic:            
                dic[num[i]] = i
         
        return []
    

'''
Solution - Naive:
1. Go through the nums list - ith number: num[i]
2. Find if there is a number
that can make the target when added up with num[i]
in the rest of the list, which is target-num[i]: num2.
3. If there is, find the index of num2 in the rest of the list, and return it with the index i.
* Cannot do nums.index(num2) in case there are duplicates.
However, nums[i+1].index(num2) returns the new index,
so need to add up the current index of which 'n' is tracking of.

Complexity - Naive:
In the worst case, the time complexity is n-1+n-2+...+1 = O(n^2) to find the num2.
To find the index of num2, it takes O(n). Thus, O(n^2 + n) = O(n^2).
The space complexity is O(n+I) = O(n).

Solution - Hash:
1. Create a dictionary(=Hash Table): dic.
2. Go through the nums list - ith number: num[i]
3. Find if the number
that can make the target, which is target-num[i]: num2,
in the dic.
4. If there is, return the value of the dic with the key - num2(dic[num2]), and the index i. 
5. If there isn't, save the (num[i]: i) key-value pair to the dic.
*As going through the nums list, the dic functions to remember the numbers in the past as well as the indices of the numbers. 
*In case there are duplicates, the dic only holds the first index as the value for a given number. 

Complexity - Hash:
The time complexity is O(n) to go through the nums list. 
The space complexity is O(2n) = O(n). 
'''
