# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curl = head
        while(curl):
            tmp = curl.next
            curl.next = prev
            prev = curl
            curl = tmp
        return head = prev
        ########## method2 #####
