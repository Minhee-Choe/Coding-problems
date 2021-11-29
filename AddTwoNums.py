'''
Source:
https://leetcode.com/problems/add-two-numbers/solution/

Problem:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        if l1 == None and l2 == None:
            return

        carry = 0
        res = resCur = ListNode()
        
        while l1 or l2 or carry!=0:
            cur1 = l1.val if l1 else 0
            cur2 = l2.val if l2 else 0

            carry, sumVal = divmod(cur1+cur2+carry,10)

            resCur.next = ListNode(sumVal)
            resCur = resCur.next
            
                     
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return res.next

'''
Solution:
Go through at the two linked lists at the same time, sum the two values, and save it to the new linked list.  
*Need to check whether there is a carry-over or not.
'''

        
